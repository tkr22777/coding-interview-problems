"""
LRU Cache (Least Recently Used Cache)
Design a data structure that implements an LRU cache with:
- set(key, value): Set key-value pair in cache
- get(key): Get value for key or None if not found

When cache reaches capacity, remove least recently used item.
Time Complexity: O(1) for all operations
Space Complexity: O(capacity) to store up to capacity elements
"""

from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_hash_map = OrderedDict()

    def set(self, key: str, value: str) -> str :
        if key in self.linked_hash_map:
            self.linked_hash_map.move_to_end(key)
        # If cache is full, remove least recently used item (first item)
        elif len(self.linked_hash_map) == self.capacity:
            self.linked_hash_map.popitem(last=False)

        # Add/update the key-value pair
        self.linked_hash_map[key] = value
        return value

    def get(self, key: str) -> Optional[str] :
        if key in self.linked_hash_map:
            # Mark as most recently used
            self.linked_hash_map.move_to_end(key)
            return self.linked_hash_map[key]
        else:
            return None

    # returns number of objects currently in the LRU cache
    def get_count(self) -> int:
        return len(self.linked_hash_map)

    def get_capacity(self) -> int:
        return self.capacity


def test_lru_cache():
    """Test LRU cache implementation with various operations."""
    # Test 1: Basic set/get operations and capacity
    cache = LRUCache(2)
    cache.set("a", "1")
    cache.set("b", "2")
    
    assert cache.get("a") == "1", "Failed to retrieve key 'a'"
    assert cache.get("b") == "2", "Failed to retrieve key 'b'"
    assert cache.get_count() == 2, "Cache count should be 2"
    
    # Test 2: Eviction of least recently used item
    cache.set("c", "3")
    assert cache.get("a") is None, "Key 'a' should have been evicted"
    assert cache.get("b") == "2", "Key 'b' should still be in cache"
    assert cache.get("c") == "3", "Key 'c' should be in cache"
    
    # Test 3: Accessing an item makes it most recently used
    cache.get("b")  # Access 'b', making it most recently used
    cache.set("d", "4")  # Should evict 'c', not 'b'
    assert cache.get("c") is None, "Key 'c' should have been evicted"
    assert cache.get("b") == "2", "Key 'b' should still be in cache"
    assert cache.get("d") == "4", "Key 'd' should be in cache"
    
    # Test 4: Updating an existing key
    cache.set("b", "5")  # Update value of 'b'
    assert cache.get("b") == "5", "Value of 'b' should be updated to '5'"
    assert cache.get_count() == 2, "Cache count should still be 2"
    
    print("All LRU cache tests passed!")


if __name__ == "__main__":
    test_lru_cache()
