"""
LFU Cache (Least Frequently Used Cache)
Design a data structure that implements an LFU cache with:
- set(key, value): Set key-value pair in cache
- get(key): Get value for key or None if not found

When cache reaches capacity, remove least frequently used item.
If multiple items have same frequency, remove the least recently used one.
"""

from typing import Optional
import heapq
from datetime import datetime

# https://leetcode.com/problems/lfu-cache/
# we need to store: key, value, frequency, last_used
# store key -> value, frequency and last_used data mapping in a dict
# store frequency and timestamp on an heap

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.frequency = 1
        self.timestamp = datetime.now()

    def increment_usage(self):
        self.frequency += 1
        self.timestamp = datetime.now()
    
    def __lt__(self, other):
        if self.frequency != other.frequency:
            return self.frequency < other.frequency
        else:
            return self.timestamp < other.timestamp

class LFUCache:

    # least frequently used, in case of tie, least recenty used
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.heap = []
 
    def set(self, key: str, value: str) -> str :
        if key in self.map:
            val_entry = self.map[key] # type: Entry
            val_entry.value = value
            val_entry.increment_usage()
            # re-heapifying as frequency and timestamp have been updated
            heapq.heapify(self.heap)
        else:
            # re-heapifying in-case get calls updated frequency, timestamp
            heapq.heapify(self.heap)

            if len(self.map) == self.capacity:
                del_entry = heapq.heappop(self.heap)
                del self.map[del_entry.key]

            val_entry = Entry(key, value)
            self.map[key] = val_entry
            heapq.heappush(self.heap, val_entry)

        # print("usage: " + str(val_entry.usage))
        # print("timestamp:" + str(val_entry.timestamp))
        return value

    def get(self, key: str) -> Optional[str] :
        if key in self.map:
            val_entry = self.map[key]
            val_entry.increment_usage()
            # heapq.heapify(self.heap), avoiding heapfy during read
            return val_entry.value
        else: 
            return None

def test_lfu_cache():
    # Test 1: Basic operations
    cache = LFUCache(2)
    cache.set("a", "a1")
    cache.set("a", "a2")  # Update existing key
    assert cache.get("a") == "a2", "Failed to update existing key"
    
    # Test 2: LFU eviction
    cache.set("b", "b1")
    assert cache.get("a") == "a2", "Failed to retrieve key 'a'"
    assert cache.get("b") == "b1", "Failed to retrieve key 'b'"
    
    # Test 3: Eviction with frequency tie
    # At this point: 'a' accessed 3 times, 'b' accessed 2 times
    cache.set("c", "c1")  # 'b' should be evicted (lower frequency than 'a')
    assert cache.get("c") == "c1", "Failed to add new key 'c'"
    assert cache.get("b") is None, "Key 'b' should have been evicted"
    
    # Test 4: Eviction with recency
    cache.get("c")  # Increase 'c' frequency
    cache.get("c")  # Now 'c' has higher frequency than 'a'
    cache.set("d", "d1")  # 'a' should be evicted (lower frequency than 'c')
    assert cache.get("a") is None, "Key 'a' should have been evicted"
    assert cache.get("d") == "d1", "Failed to add new key 'd'"
    assert cache.get("c") == "c1", "Failed to retain key 'c' with highest frequency"
    
    print("All LFU Cache tests passed!")


if __name__ == "__main__":
    test_lfu_cache()