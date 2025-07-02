from threading import Lock
from typing import Any, Optional, Dict
import time
from cache.cache_interface import CacheInterface

class CacheEntry:
    """Represents a cache entry with optional expiration."""
    def __init__(self, value: Any, expiry: Optional[float] = None):
        self.value = value
        self.expiry = expiry
        self.last_accessed = time.time()

class ThreadedCache(CacheInterface):
    """A thread-safe LRU cache implementation."""
    
    def __init__(self, max_size: int = 1000):
        """
        Initialize the cache.
        
        Args:
            max_size: Maximum number of items to store (default: 1000)
        """
        if max_size <= 0:
            raise ValueError("max_size must be positive")
            
        self.max_size = max_size
        
        # Internal state
        self.__cache: Dict[str, tuple[Any, float]] = {}  # {key: (value, expiry)}
        self.__total_puts = 0
        self.__total_gets = 0
        self.__hits = 0
        self.__misses = 0
        self.__evictions = 0
        
        # Synchronization primitives
        self.__lock = Lock()
    
    def put(self, key: str, value: Any, ttl_seconds: Optional[float] = None) -> None:
        """
        Add or update an item in the cache.
        
        Args:
            key: Key to store the value under
            value: Value to store
            ttl_seconds: Optional time-to-live in seconds
        """
        with self.__lock:
            # Increment puts counter
            self.__total_puts += 1
            
            # Calculate expiry time
            expiry = time.time() + ttl_seconds if ttl_seconds is not None else None
            
            # If key exists, just update it
            if key in self.__cache:
                self.__cache[key] = (value, expiry)
                return
            
            # If cache is full, evict oldest item
            if len(self.__cache) >= self.max_size:
                oldest_key = min(self.__cache.keys(), 
                               key=lambda k: self.__cache[k][1] or float('inf'))
                del self.__cache[oldest_key]
                self.__evictions += 1
            
            # Add new item
            self.__cache[key] = (value, expiry)
    
    def get(self, key: str) -> Optional[Any]:
        """
        Get an item from the cache.
        
        Args:
            key: Key to look up
            
        Returns:
            The value if found and not expired, None otherwise
        """
        with self.__lock:
            # Increment gets counter
            self.__total_gets += 1
            
            # Check if key exists
            if key not in self.__cache:
                self.__misses += 1
                return None
            
            value, expiry = self.__cache[key]
            
            # Check if expired
            if expiry is not None and time.time() > expiry:
                del self.__cache[key]
                self.__misses += 1
                return None
            
            # Record hit and return value
            self.__hits += 1
            return value
    
    def remove(self, key: str) -> bool:
        """
        Remove an item from the cache.
        
        Args:
            key: Key to remove
            
        Returns:
            True if the key was found and removed, False otherwise
        """
        with self.__lock:
            if key in self.__cache:
                del self.__cache[key]
                return True
            return False
    
    def clear(self) -> None:
        """Clear all items from the cache."""
        with self.__lock:
            self.__cache.clear()
    
    def get_stats(self) -> dict:
        """
        Get cache statistics.
        
        Returns:
            Dict containing:
            - size: Current number of items
            - max_size: Maximum number of items
            - total_puts: Total number of puts
            - total_gets: Total number of gets
            - hits: Number of cache hits
            - misses: Number of cache misses
            - evictions: Number of items evicted
        """
        with self.__lock:
            return {
                'size': len(self.__cache),
                'max_size': self.max_size,
                'total_puts': self.__total_puts,
                'total_gets': self.__total_gets,
                'hits': self.__hits,
                'misses': self.__misses,
                'evictions': self.__evictions
            }
    
    def _evict_lru(self) -> None:
        """Evict the least recently used item from the cache."""
        if not self.__cache:
            return
            
        # Find LRU entry
        lru_key = min(self.__cache.keys(), 
                     key=lambda k: self.__cache[k][1] or float('inf'))
        
        # Remove it
        del self.__cache[lru_key]
        self.__evictions += 1 