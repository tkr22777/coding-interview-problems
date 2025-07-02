from abc import ABC, abstractmethod
from typing import Optional

class CounterInterface(ABC):
    """Interface for a thread-safe and process-safe counter."""
    
    @abstractmethod
    def increment(self, amount: int = 1) -> int:
        """
        Increment the counter by the given amount.
        
        Args:
            amount: Amount to increment by (default: 1)
            
        Returns:
            The new counter value
            
        Raises:
            ValueError: If incrementing would exceed max_value
        """
        pass
    
    @abstractmethod
    def decrement(self, amount: int = 1) -> int:
        """
        Decrement the counter by the given amount.
        
        Args:
            amount: Amount to decrement by (default: 1)
            
        Returns:
            The new counter value
            
        Raises:
            ValueError: If decrementing would go below min_value
        """
        pass
    
    @abstractmethod
    def get_value(self) -> int:
        """Get the current counter value."""
        pass
    
    @abstractmethod
    def reset(self) -> None:
        """Reset the counter to its initial value."""
        pass
    
    @abstractmethod
    def compare_and_set(self, expected: int, new_value: int) -> bool:
        """
        Atomically set the counter to new_value if it currently equals expected.
        
        Args:
            expected: The expected current value
            new_value: The new value to set if expected matches current
            
        Returns:
            True if the value was updated, False otherwise
            
        Raises:
            ValueError: If new_value is outside valid range
        """
        pass
    
    @abstractmethod
    def get_stats(self) -> dict:
        """
        Get counter statistics.
        
        Returns:
            Dict containing:
            - value: Current counter value
            - min_seen: Minimum value seen
            - max_seen: Maximum value seen
            - total_increments: Number of successful increments
            - total_decrements: Number of successful decrements
            - failed_updates: Number of failed updates (exceeded bounds)
        """
        pass 