from multiprocessing import Lock, Condition
from typing import Any, Optional, Dict, List
import time
from bounded_queue.queue_interface import QueueInterface

class MultiprocessQueue(QueueInterface):
    """A process-safe bounded queue implementation using external shared state."""
    
    def __init__(self, shared_data: List, shared_stats: Dict, shared_lock: Lock, shared_conditions: Dict, max_size: int = 100):
        """
        Initialize the queue with external shared state.
        
        Args:
            shared_data: Shared list for queue data
            shared_stats: Shared dictionary for statistics
            shared_lock: Shared lock for synchronization
            shared_conditions: Dict with 'not_full' and 'not_empty' condition variables
            max_size: Maximum number of items to store
        """
        if max_size <= 0:
            raise ValueError("max_size must be positive")
            
        self.max_size = max_size
        self.__shared_data = shared_data  # External shared queue data
        self.__shared_stats = shared_stats  # External shared statistics
        self.__lock = shared_lock  # External shared lock
        self.__not_full = shared_conditions['not_full']
        self.__not_empty = shared_conditions['not_empty']
        
        # Initialize stats if not already done
        with self.__lock:
            if 'total_puts' not in self.__shared_stats:
                self.__shared_stats.update({
                    'total_puts': 0,
                    'total_gets': 0,
                    'put_timeouts': 0,
                    'get_timeouts': 0
                })
    
    def put(self, item: Any, timeout: Optional[float] = None) -> bool:
        """Add an item to the queue."""
        end_time = time.time() + timeout if timeout is not None else None
        
        with self.__lock:
            while len(self.__shared_data) >= self.max_size:
                if timeout is not None:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        self.__shared_stats['put_timeouts'] += 1
                        return False
                    if not self.__not_full.wait(remaining):
                        self.__shared_stats['put_timeouts'] += 1
                        return False
                else:
                    self.__not_full.wait()
            
            self.__shared_data.append(item)
            self.__shared_stats['total_puts'] += 1
            self.__not_empty.notify()
            return True
    
    def get(self, timeout: Optional[float] = None) -> Optional[Any]:
        """Get an item from the queue."""
        end_time = time.time() + timeout if timeout is not None else None
        
        with self.__lock:
            while len(self.__shared_data) == 0:
                if timeout is not None:
                    remaining = end_time - time.time()
                    if remaining <= 0:
                        self.__shared_stats['get_timeouts'] += 1
                        return None
                    if not self.__not_empty.wait(remaining):
                        self.__shared_stats['get_timeouts'] += 1
                        return None
                else:
                    self.__not_empty.wait()
            
            item = self.__shared_data.pop(0)
            self.__shared_stats['total_gets'] += 1
            self.__not_full.notify()
            return item
    
    def get_stats(self) -> dict:
        """Get queue statistics."""
        with self.__lock:
            return {
                'size': len(self.__shared_data),
                'max_size': self.max_size,
                'total_puts': self.__shared_stats['total_puts'],
                'total_gets': self.__shared_stats['total_gets'],
                'put_timeouts': self.__shared_stats['put_timeouts'],
                'get_timeouts': self.__shared_stats['get_timeouts']
            }
    
    def size(self) -> int:
        """Get the current number of items in the queue."""
        with self.__lock:
            return len(self.__shared_data)
    
    def clear(self) -> None:
        """Clear all items from the queue."""
        with self.__lock:
            self.__shared_data[:] = []  # Clear the shared list in place
            self.__not_full.notify_all() 