from multiprocessing import Lock
from typing import Any, Optional, Dict
import time
import pickle
from cache.cache_interface import CacheInterface

class MultiprocessCache(CacheInterface):
    """A process-safe LRU cache implementation using external shared state."""
    
    def __init__(self, shared_data: Dict, shared_stats: Dict, shared_lock: Lock, max_size: int = 1000):
        """
        Initialize the cache with external shared state.
        
        Args:
            shared_data: Shared dictionary for cache data
            shared_stats: Shared dictionary for statistics
            shared_lock: Shared lock for synchronization
            max_size: Maximum number of items to store
        """
        if max_size <= 0:
            raise ValueError("max_size must be positive")
            
        self.max_size = max_size
        self.__shared_data = shared_data  # External shared cache data
        self.__shared_stats = shared_stats  # External shared statistics
        self.__lock = shared_lock  # External shared lock
        
        # Initialize stats if not already done
        with self.__lock:
            if 'total_puts' not in self.__shared_stats:
                self.__shared_stats.update({
                    'total_puts': 0,
                    'total_gets': 0,
                    'hits': 0,
                    'misses': 0,
                    'evictions': 0
                })
    
    def put(self, key: str, value: Any, ttl_seconds: Optional[float] = None) -> None:
        """Add or update an item in the cache."""
        with self.__lock:
            # Increment puts counter
            self.__shared_stats['total_puts'] += 1
            
            # Calculate expiry time
            expiry = time.time() + ttl_seconds if ttl_seconds is not None else None
            
            # If key exists, just update it
            if key in self.__shared_data:
                self.__shared_data[key] = (value, expiry)
                return
            
            # If cache is full, evict oldest item (LRU approximation using expiry times)
            if len(self.__shared_data) >= self.max_size:
                # Find item with earliest expiry (or no expiry = oldest)
                oldest_key = min(self.__shared_data.keys(), 
                               key=lambda k: self.__shared_data[k][1] or 0)
                del self.__shared_data[oldest_key]
                self.__shared_stats['evictions'] += 1
            
            # Add new item
            self.__shared_data[key] = (value, expiry)
    
    def get(self, key: str) -> Optional[Any]:
        """Get an item from the cache."""
        with self.__lock:
            # Increment gets counter
            self.__shared_stats['total_gets'] += 1
            
            # Check if key exists
            if key not in self.__shared_data:
                self.__shared_stats['misses'] += 1
                return None
            
            value, expiry = self.__shared_data[key]
            
            # Check if expired
            if expiry is not None and time.time() > expiry:
                del self.__shared_data[key]
                self.__shared_stats['misses'] += 1
                return None
            
            # Record hit and return value
            self.__shared_stats['hits'] += 1
            return value
    
    def get_stats(self) -> dict:
        """Get cache statistics."""
        with self.__lock:
            return {
                'size': len(self.__shared_data),
                'max_size': self.max_size,
                'total_puts': self.__shared_stats['total_puts'],
                'total_gets': self.__shared_stats['total_gets'],
                'hits': self.__shared_stats['hits'],
                'misses': self.__shared_stats['misses'],
                'evictions': self.__shared_stats['evictions']
            }
    
    def remove(self, key: str) -> bool:
        """Remove an item from the cache."""
        with self.__lock:
            if key in self.__shared_data:
                del self.__shared_data[key]
                return True
            return False
    
    def clear(self) -> None:
        """Clear all items from the cache."""
        with self.__lock:
            self.__shared_data.clear() 