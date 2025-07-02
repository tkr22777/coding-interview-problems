from multiprocessing import Lock
from typing import Dict
from counter.counter_interface import CounterInterface

class MultiprocessCounter(CounterInterface):
    """A process-safe atomic counter implementation using external shared state."""
    
    def __init__(self, shared_value: Dict, shared_stats: Dict, shared_lock: Lock, min_value: int = None, max_value: int = None):
        """
        Initialize the counter with external shared state.
        
        Args:
            shared_value: Shared dictionary containing the counter value
            shared_stats: Shared dictionary for statistics
            shared_lock: Shared lock for synchronization
            min_value: Optional minimum value
            max_value: Optional maximum value
        """
        self.min_value = min_value
        self.max_value = max_value
        self.__shared_value = shared_value  # External shared counter value
        self.__shared_stats = shared_stats  # External shared statistics
        self.__lock = shared_lock  # External shared lock
        
        # Initialize value and stats if not already done
        with self.__lock:
            if 'value' not in self.__shared_value:
                self.__shared_value['value'] = 0
            if 'increments' not in self.__shared_stats:
                self.__shared_stats.update({
                    'increments': 0,
                    'decrements': 0,
                    'gets': 0,
                    'resets': 0,
                    'min_seen': self.__shared_value['value'],
                    'max_seen': self.__shared_value['value'],
                    'failed_updates': 0
                })
    
    def increment(self, amount: int = 1) -> int:
        """Increment the counter by the given amount."""
        with self.__lock:
            new_value = self.__shared_value['value'] + amount
            if self.max_value is not None and new_value > self.max_value:
                self.__shared_stats['failed_updates'] += 1
                raise ValueError(f"Increment by {amount} would exceed maximum value {self.max_value}")
            
            self.__shared_value['value'] = new_value
            self.__shared_stats['increments'] += 1
            
            # Update min/max seen
            if new_value > self.__shared_stats['max_seen']:
                self.__shared_stats['max_seen'] = new_value
            if new_value < self.__shared_stats['min_seen']:
                self.__shared_stats['min_seen'] = new_value
                
            return new_value
    
    def decrement(self, amount: int = 1) -> int:
        """Decrement the counter by the given amount."""
        with self.__lock:
            new_value = self.__shared_value['value'] - amount
            if self.min_value is not None and new_value < self.min_value:
                self.__shared_stats['failed_updates'] += 1
                raise ValueError(f"Decrement by {amount} would go below minimum value {self.min_value}")
            
            self.__shared_value['value'] = new_value
            self.__shared_stats['decrements'] += 1
            
            # Update min/max seen
            if new_value > self.__shared_stats['max_seen']:
                self.__shared_stats['max_seen'] = new_value
            if new_value < self.__shared_stats['min_seen']:
                self.__shared_stats['min_seen'] = new_value
                
            return new_value
    
    def get_value(self) -> int:
        """Get the current value."""
        with self.__lock:
            self.__shared_stats['gets'] += 1
            return self.__shared_value['value']
    
    def get(self) -> int:
        """Get the current value (alias for get_value)."""
        return self.get_value()
    
    def reset(self) -> None:
        """Reset the counter to 0."""
        with self.__lock:
            self.__shared_value['value'] = 0
            self.__shared_stats['resets'] += 1
    
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
        with self.__lock:
            # Validate new value first
            if self.min_value is not None and new_value < self.min_value:
                self.__shared_stats['failed_updates'] += 1
                raise ValueError(f"New value {new_value} is below minimum {self.min_value}")
            if self.max_value is not None and new_value > self.max_value:
                self.__shared_stats['failed_updates'] += 1
                raise ValueError(f"New value {new_value} is above maximum {self.max_value}")
            
            # Compare and set
            if self.__shared_value['value'] == expected:
                self.__shared_value['value'] = new_value
                
                # Update min/max seen
                if new_value > self.__shared_stats['max_seen']:
                    self.__shared_stats['max_seen'] = new_value
                if new_value < self.__shared_stats['min_seen']:
                    self.__shared_stats['min_seen'] = new_value
                    
                return True
            else:
                self.__shared_stats['failed_updates'] += 1
                return False
    
    def get_stats(self) -> dict:
        """Get counter statistics."""
        with self.__lock:
            return {
                'value': self.__shared_value['value'],
                'increments': self.__shared_stats['increments'],
                'decrements': self.__shared_stats['decrements'],
                'gets': self.__shared_stats['gets'],
                'resets': self.__shared_stats['resets'],
                'min_seen': self.__shared_stats['min_seen'],
                'max_seen': self.__shared_stats['max_seen'],
                'failed_updates': self.__shared_stats['failed_updates']
            } 