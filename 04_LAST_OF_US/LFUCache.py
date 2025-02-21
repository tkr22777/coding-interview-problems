import unittest
from typing import Optional
import heapq
from datetime import datetime


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

cache = LFUCache(2)
cache.set("a", "a1")
cache.set("a", "a2")
print(cache.get('a') == "a2")
cache.set("b", "b1")
print(cache.get('a') == "a2")
print(cache.get('b') == "b1")
# b should be removed,
# key 'a' has been accessed 4 times,
# key 'b' has been accessed 3 times
cache.set("c", "c1") 
print(cache.get('c') == "c1")
print(cache.get('b') is None)
cache.get("c")
cache.get("c")
cache.set("d", "d1")
print(cache.get("a") is None)
print(cache.get('d') == "d1")
print(cache.get('c') == "c1")