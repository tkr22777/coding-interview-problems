from multiprocessing import Lock, Condition
from typing import Any, Optional, Dict, List
import time
from contextlib import contextmanager
from resource_pool.pool_interface import PoolInterface

class MultiprocessPool(PoolInterface):
    """A process-safe resource pool implementation using external shared state."""
    
    def __init__(self, shared_resources: List, shared_available: List, shared_stats: Dict, 
                 shared_lock: Lock, shared_condition: Condition, max_size: int = None):
        """
        Initialize the pool with external shared state.
        
        Args:
            shared_resources: Shared list of all resources
            shared_available: Shared list of available resource indices
            shared_stats: Shared dictionary for statistics
            shared_lock: Shared lock for synchronization
            shared_condition: Shared condition variable for blocking operations
            max_size: Maximum number of resources in the pool
        """
        self.max_size = max_size
        self.__shared_resources = shared_resources  # External shared resources
        self.__shared_available = shared_available  # External shared available indices
        self.__shared_stats = shared_stats  # External shared statistics
        self.__lock = shared_lock  # External shared lock
        self.__condition = shared_condition  # External shared condition
        
        # Initialize stats if not already done
        with self.__lock:
            if 'total_acquires' not in self.__shared_stats:
                self.__shared_stats.update({
                    'total_acquires': 0,
                    'total_releases': 0,
                    'acquire_timeouts': 0,
                    'failed_validations': 0
                })
    
    def acquire(self, timeout: Optional[float] = None) -> Optional[Any]:
        """Acquire a resource from the pool."""
        end_time = time.time() + timeout if timeout is not None else None
        
        with self.__lock:
            while not self.__shared_available:
                if timeout is not None:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        self.__shared_stats['acquire_timeouts'] += 1
                        return None
                    if not self.__condition.wait(remaining):
                        self.__shared_stats['acquire_timeouts'] += 1
                        return None
                else:
                    self.__condition.wait()
            
            # Get an available resource
            resource_idx = self.__shared_available.pop()
            resource = self.__shared_resources[resource_idx]
            self.__shared_stats['total_acquires'] += 1
            return resource
    
    def release(self, resource: Any) -> bool:
        """Release a resource back to the pool."""
        if resource is None:
            raise ValueError("Cannot release None resource")
            
        with self.__lock:
            # Find the resource index
            try:
                resource_idx = None
                for i, res in enumerate(self.__shared_resources):
                    if str(res) == str(resource):  # Compare string representations for multiprocess safety
                        resource_idx = i
                        break
                
                if resource_idx is None:
                    self.__shared_stats['failed_validations'] += 1
                    return False
                
                # Check if already available
                if resource_idx in self.__shared_available:
                    self.__shared_stats['failed_validations'] += 1
                    return False
                
                # Return to available pool
                self.__shared_available.append(resource_idx)
                self.__shared_stats['total_releases'] += 1
                self.__condition.notify()
                return True
                
            except Exception:
                self.__shared_stats['failed_validations'] += 1
                return False
    
    def add_resource(self, resource: Any) -> bool:
        """Add a new resource to the pool."""
        if resource is None:
            raise ValueError("Cannot add None resource")
            
        with self.__lock:
            # Check if pool is full
            if self.max_size is not None and len(self.__shared_resources) >= self.max_size:
                return False
            
            # Check if resource already exists
            for res in self.__shared_resources:
                if str(res) == str(resource):
                    return False
            
            # Add resource
            self.__shared_resources.append(resource)
            self.__shared_available.append(len(self.__shared_resources) - 1)
            self.__condition.notify()
            return True
    
    def remove_resource(self, resource: Any) -> bool:
        """Remove a resource from the pool."""
        with self.__lock:
            # Find the resource index
            resource_idx = None
            for i, res in enumerate(self.__shared_resources):
                if str(res) == str(resource):
                    resource_idx = i
                    break
            
            if resource_idx is None:
                return False
            
            # Remove from available list if present
            if resource_idx in self.__shared_available:
                self.__shared_available.remove(resource_idx)
            
            # Remove from resources and adjust indices
            self.__shared_resources.pop(resource_idx)
            
            # Update available indices (all indices >= resource_idx need to be decremented)
            updated_available = []
            for idx in self.__shared_available:
                if idx > resource_idx:
                    updated_available.append(idx - 1)
                else:
                    updated_available.append(idx)
            self.__shared_available[:] = updated_available
            
            return True
    
    @contextmanager
    def acquire_context(self, timeout: Optional[float] = None):
        """Context manager for acquiring and releasing resources."""
        resource = self.acquire(timeout)
        if resource is None:
            raise TimeoutError("Failed to acquire resource within timeout")
        try:
            yield resource
        finally:
            self.release(resource)
    
    def get_stats(self) -> dict:
        """Get pool statistics."""
        with self.__lock:
            return {
                'total_resources': len(self.__shared_resources),
                'available_resources': len(self.__shared_available),
                'total_acquires': self.__shared_stats['total_acquires'],
                'total_releases': self.__shared_stats['total_releases'],
                'acquire_timeouts': self.__shared_stats['acquire_timeouts'],
                'failed_validations': self.__shared_stats['failed_validations']
            } 