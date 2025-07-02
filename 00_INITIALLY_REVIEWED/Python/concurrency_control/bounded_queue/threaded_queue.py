from threading import Lock, Condition
from typing import Any, Optional, List
import time
from bounded_queue.queue_interface import QueueInterface

class ThreadedQueue(QueueInterface):
    """A thread-safe bounded queue implementation."""
    
    def __init__(self, max_size: int = 100):
        """
        Initialize the queue.
        
        Args:
            max_size: Maximum number of items the queue can hold (default: 100)
        """
        if max_size <= 0:
            raise ValueError("max_size must be positive")
            
        self.max_size = max_size
        
        # Internal state
        self.__queue: List[Any] = []
        self.__total_puts = 0
        self.__total_gets = 0
        self.__put_timeouts = 0
        self.__get_timeouts = 0
        
        # Synchronization primitives
        self.__lock = Lock()
        self.__not_empty = Condition(self.__lock)
        self.__not_full = Condition(self.__lock)
    
    def put(self, item: Any, timeout: Optional[float] = None) -> bool:
        """
        Put an item in the queue.
        
        Args:
            item: Item to put in the queue
            timeout: Optional timeout in seconds
            
        Returns:
            True if item was added, False if timed out
        """
        with self.__lock:
            if timeout is not None:
                end_time = time.time() + timeout
            
            while len(self.__queue) >= self.max_size:
                if timeout is not None:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        self.__put_timeouts += 1
                        return False
                    self.__not_full.wait(timeout=remaining)
                else:
                    self.__not_full.wait()
            
            self.__queue.append(item)
            self.__total_puts += 1
            self.__not_empty.notify()
            return True
    
    def get(self, timeout: Optional[float] = None) -> Optional[Any]:
        """
        Get an item from the queue.
        
        Args:
            timeout: Optional timeout in seconds
            
        Returns:
            The item if one was available, None if timed out
        """
        with self.__lock:
            if timeout is not None:
                end_time = time.time() + timeout
            
            while not self.__queue:
                if timeout is not None:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        self.__get_timeouts += 1
                        return None
                    self.__not_empty.wait(timeout=remaining)
                else:
                    self.__not_empty.wait()
            
            item = self.__queue.pop(0)
            self.__total_gets += 1
            self.__not_full.notify()
            return item
    
    def get_stats(self) -> dict:
        """
        Get queue statistics.
        
        Returns:
            Dict containing:
            - size: Current number of items
            - max_size: Maximum number of items
            - total_puts: Total number of puts
            - total_gets: Total number of gets
            - put_timeouts: Number of put timeouts
            - get_timeouts: Number of get timeouts
        """
        with self.__lock:
            return {
                'size': len(self.__queue),
                'max_size': self.max_size,
                'total_puts': self.__total_puts,
                'total_gets': self.__total_gets,
                'put_timeouts': self.__put_timeouts,
                'get_timeouts': self.__get_timeouts
            }
    
    def size(self) -> int:
        """
        Get the current number of items in the queue.
        
        Returns:
            Number of items currently in the queue
        """
        with self.__lock:
            return len(self.__queue)
    
    def clear(self) -> None:
        """Clear all items from the queue."""
        with self.__lock:
            self.__queue.clear()
            self.__not_full.notify_all() 