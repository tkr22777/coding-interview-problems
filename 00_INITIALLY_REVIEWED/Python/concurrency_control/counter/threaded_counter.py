from threading import Lock
from typing import Optional
from counter.counter_interface import CounterInterface

class ThreadedCounter(CounterInterface):
    """A thread-safe counter implementation."""
    
    def __init__(self, initial_value: int = 0, min_value: Optional[int] = None, max_value: Optional[int] = None):
        """
        Initialize the counter.
        
        Args:
            initial_value: Starting value for counter
            min_value: Optional minimum value (inclusive)
            max_value: Optional maximum value (inclusive)
        """
        self.min_value = min_value
        self.max_value = max_value
        self.initial_value = initial_value
        
        # Validate initial value
        if min_value is not None and initial_value < min_value:
            raise ValueError(f"Initial value {initial_value} is less than minimum {min_value}")
        if max_value is not None and initial_value > max_value:
            raise ValueError(f"Initial value {initial_value} is greater than maximum {max_value}")
        
        # Internal state
        self.__value = initial_value
        self.__min_seen = initial_value
        self.__max_seen = initial_value
        self.__total_increments = 0
        self.__total_decrements = 0
        self.__failed_updates = 0
        self.__lock = Lock()
    
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
        with self.__lock:
            new_value = self.__value + amount
            if self.max_value is not None and new_value > self.max_value:
                self.__failed_updates += 1
                raise ValueError(f"Increment by {amount} would exceed maximum {self.max_value}")
            self.__value = new_value
            self.__total_increments += 1
            if new_value > self.__max_seen:
                self.__max_seen = new_value
            return new_value
    
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
        with self.__lock:
            new_value = self.__value - amount
            if self.min_value is not None and new_value < self.min_value:
                self.__failed_updates += 1
                raise ValueError(f"Decrement by {amount} would go below minimum {self.min_value}")
            self.__value = new_value
            self.__total_decrements += 1
            if new_value < self.__min_seen:
                self.__min_seen = new_value
            return new_value
    
    def get_value(self) -> int:
        """Get current counter value."""
        with self.__lock:
            return self.__value
    
    def reset(self) -> None:
        """Reset the counter to its initial value."""
        with self.__lock:
            self.__value = self.initial_value
    
    def compare_and_set(self, expected: int, new_value: int) -> bool:
        """
        Set value only if current value matches expected.
        
        Args:
            expected: Value to compare against
            new_value: Value to set if comparison succeeds
            
        Returns:
            bool: True if value was set, False otherwise
            
        Raises:
            ValueError: If new_value is outside valid range
        """
        if self.min_value is not None and new_value < self.min_value:
            self.__failed_updates += 1
            raise ValueError(f"New value {new_value} is below minimum {self.min_value}")
        if self.max_value is not None and new_value > self.max_value:
            self.__failed_updates += 1
            raise ValueError(f"New value {new_value} is above maximum {self.max_value}")
            
        with self.__lock:
            if self.__value == expected:
                self.__value = new_value
                if new_value > self.__max_seen:
                    self.__max_seen = new_value
                if new_value < self.__min_seen:
                    self.__min_seen = new_value
                return True
            self.__failed_updates += 1
            return False
    
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
        with self.__lock:
            return {
                'value': self.__value,
                'min_seen': self.__min_seen,
                'max_seen': self.__max_seen,
                'total_increments': self.__total_increments,
                'total_decrements': self.__total_decrements,
                'failed_updates': self.__failed_updates
            } 