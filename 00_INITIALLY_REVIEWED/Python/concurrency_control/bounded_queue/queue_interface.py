from abc import ABC, abstractmethod
from typing import Any, Optional

class QueueInterface(ABC):
    """Interface for a bounded queue implementation."""
    
    @abstractmethod
    def put(self, item: Any, timeout: Optional[float] = None) -> bool:
        """
        Put an item in the queue.
        
        Args:
            item: Item to put in queue
            timeout: Maximum time to wait in seconds
            
        Returns:
            bool: True if successful, False if timeout
        """
        pass
    
    @abstractmethod
    def get(self, timeout: Optional[float] = None) -> Optional[Any]:
        """
        Get an item from the queue.
        
        Args:
            timeout: Maximum time to wait in seconds
            
        Returns:
            Any: Item from queue, or None if timeout
        """
        pass
    
    @abstractmethod
    def size(self) -> int:
        """
        Get current size of queue.
        
        Returns:
            int: Number of items in queue
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Clear all items from queue."""
        pass
    
    @abstractmethod
    def get_stats(self) -> dict:
        """
        Get queue statistics.
        
        Returns:
            dict: Dictionary containing queue statistics
        """
        pass 