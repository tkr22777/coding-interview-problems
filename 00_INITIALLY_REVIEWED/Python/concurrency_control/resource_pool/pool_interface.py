from abc import ABC, abstractmethod
from typing import Any, Optional, Callable, TypeVar, Generic, List

T = TypeVar('T')  # Type of resource managed by the pool

class PoolInterface(Generic[T], ABC):
    """Interface for a thread-safe and process-safe resource pool."""
    
    @abstractmethod
    def acquire(self, timeout: Optional[float] = None) -> Optional[T]:
        """
        Acquire a resource from the pool.
        
        Args:
            timeout: Optional timeout in seconds. If None, blocks indefinitely
            
        Returns:
            A resource if one was acquired, None if timed out
        """
        pass
    
    @abstractmethod
    def release(self, resource: T) -> bool:
        """
        Return a resource to the pool.
        
        Args:
            resource: The resource to return
            
        Returns:
            True if resource was returned to pool, False if resource was invalid
            
        Raises:
            ValueError: If resource is None
        """
        pass
    
    @abstractmethod
    def add_resource(self, resource: T) -> bool:
        """
        Add a new resource to the pool.
        
        Args:
            resource: The resource to add
            
        Returns:
            True if resource was added, False if pool is full
            
        Raises:
            ValueError: If resource is None or invalid
        """
        pass
    
    @abstractmethod
    def remove_resource(self, resource: T) -> bool:
        """
        Remove a resource from the pool.
        
        Args:
            resource: The resource to remove
            
        Returns:
            True if resource was removed, False if not found
        """
        pass
    
    @abstractmethod
    def get_stats(self) -> dict:
        """
        Get pool statistics.
        
        Returns:
            Dict containing:
            - total_resources: Total number of resources in pool
            - available_resources: Number of available resources
            - total_acquires: Total number of successful acquires
            - total_releases: Total number of successful releases
            - acquire_timeouts: Number of acquire timeouts
            - failed_validations: Number of failed resource validations
        """
        pass 