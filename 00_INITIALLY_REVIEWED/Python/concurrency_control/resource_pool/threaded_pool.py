from threading import Lock, Condition
from typing import Any, Optional, Callable, TypeVar, List
import time
import random
from resource_pool.pool_interface import PoolInterface, T
from contextlib import contextmanager

def default_validate(resource: Any) -> bool:
    """Default validation function that always returns True."""
    return True

class ThreadedPool(PoolInterface[T]):
    """A thread-safe resource pool implementation."""
    
    def __init__(self, max_size: int, validate_fn: Optional[Callable[[T], bool]] = None):
        """
        Initialize the pool.
        
        Args:
            max_size: Maximum number of resources the pool can hold
            validate_fn: Optional function to validate resources before returning them to pool
        """
        if max_size <= 0:
            raise ValueError("max_size must be positive")
            
        self.max_size = max_size
        self.validate_fn = validate_fn or default_validate
        
        # Internal state
        self.__available = []  # List of available resources
        self.__all_resources = []  # List of all resources (in use or available)
        self.__total_acquires = 0
        self.__total_releases = 0
        self.__acquire_timeouts = 0
        self.__failed_validations = 0
        
        # Synchronization primitives
        self.__lock = Lock()
        self.__not_empty = Condition(self.__lock)
    
    def acquire(self, timeout: Optional[float] = None) -> Optional[T]:
        with self.__lock:
            if timeout is not None:
                end_time = time.time() + timeout
            
            while not self.__available:
                if timeout is not None:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        self.__acquire_timeouts += 1
                        return None
                    self.__not_empty.wait(timeout=remaining)
                else:
                    self.__not_empty.wait()
            
            resource = self.__available.pop()
            self.__total_acquires += 1
            return resource
    
    def release(self, resource: T) -> bool:
        if resource is None:
            raise ValueError("Cannot release None resource")
            
        with self.__lock:
            if resource not in self.__all_resources:
                return False
                
            # Validate resource before returning to pool
            if not self.validate_fn(resource):
                self.__failed_validations += 1
                return False
            
            self.__available.append(resource)
            self.__total_releases += 1
            self.__not_empty.notify()
            return True
    
    def add_resource(self, resource: T) -> bool:
        if resource is None:
            raise ValueError("Cannot add None resource")
            
        with self.__lock:
            if len(self.__all_resources) >= self.max_size:
                return False
                
            if not self.validate_fn(resource):
                self.__failed_validations += 1
                return False
                
            self.__all_resources.append(resource)
            self.__available.append(resource)
            self.__not_empty.notify()
            return True
    
    def remove_resource(self, resource: T) -> bool:
        with self.__lock:
            if resource not in self.__all_resources:
                return False
                
            self.__all_resources.remove(resource)
            if resource in self.__available:
                self.__available.remove(resource)
            return True
    
    def get_stats(self) -> dict:
        with self.__lock:
            return {
                'total_resources': len(self.__all_resources),
                'available_resources': len(self.__available),
                'total_acquires': self.__total_acquires,
                'total_releases': self.__total_releases,
                'acquire_timeouts': self.__acquire_timeouts,
                'failed_validations': self.__failed_validations
            }
    
    @contextmanager
    def acquire_context(self, timeout: Optional[float] = None):
        """Context manager for acquiring and releasing resources."""
        resource = self.acquire(timeout)
        try:
            yield resource
        finally:
            if resource is not None:
                self.release(resource) 