from abc import ABC, abstractmethod
from typing import Any, Optional
from datetime import datetime

class CacheInterface(ABC):
    """Interface for a thread-safe and process-safe cache implementation."""
    
    @abstractmethod
    def put(self, key: str, value: Any, ttl_seconds: Optional[int] = None) -> None:
        """
        Store a value in the cache with optional TTL.
        
        Args:
            key: The key to store the value under
            value: The value to store
            ttl_seconds: Optional time-to-live in seconds. If None, entry won't expire
        
        Raises:
            ValueError: If the cache is full and no items can be evicted
        """
        pass
    
    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        """
        Retrieve a value from the cache.
        
        Args:
            key: The key to look up
            
        Returns:
            The value if found and not expired, None otherwise
        """
        pass
    
    @abstractmethod
    def remove(self, key: str) -> bool:
        """
        Remove an item from the cache.
        
        Args:
            key: The key to remove
            
        Returns:
            True if the key was found and removed, False otherwise
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Remove all items from the cache."""
        pass
    
    @abstractmethod
    def get_stats(self) -> dict:
        """
        Get cache statistics.
        
        Returns:
            Dict containing:
            - size: Current number of items
            - hits: Number of cache hits
            - misses: Number of cache misses
            - evictions: Number of items evicted
        """
        pass 