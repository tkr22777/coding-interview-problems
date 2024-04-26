import unittest
from typing import Optional
import heapq
from datetime import datetime


# we need to store: key, value, frequency, last_used
# store key -> value, frequency and last_usedata mapping in a dict
# store frequency and timestamp on an heap

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.usage = 1
        self.timestamp = datetime.now()

    def increment_usage(self):
        self.usage += 1
        self.timestamp = datetime.now()
    
    def __lt__(self, other):
        if self.usage != other.usage:
            return self.usage < other.usage
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
            val_entry = self.map[key] 
            val_entry.value = value
            val_entry.increment_usage()
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

class TestLFUCache(unittest.TestCase):
    def test_set_and_get_2(self):
        cache = LFUCache(2)
        cache.set("a", "a1")
        cache.set("a", "a2")
        self.assertEqual(cache.get('a'), "a2")
        cache.set("b", "b1")
        self.assertEqual(cache.get('a'), "a2")
        self.assertEqual(cache.get('b'), "b1")
        # b should be removed,
        # key 'a' has been accessed 4 times,
        # key 'b' has been accessed 3 times
        cache.set("c", "c1") 
        self.assertEqual(cache.get('c'), "c1")
        self.assertIsNone(cache.get('b'))
        cache.get("c")
        cache.get("c")
        cache.set("d", "d1")
        self.assertIsNone(cache.get("a"))
        self.assertEqual(cache.get('d'), "d1")
        self.assertEqual(cache.get('c'), "c1")
        # self.assertIsNone(cache.get('b'))
        # self.assertEqual(cache.get('a'), "1")
        # cache.get("c")
        # cache.set("d", "4")
        # self.assertIsNone(cache.get('a'))
    
    
    def test_set_and_get(self):
        cache = LFUCache(3)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        cache.set('c', 'cherry')
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('b'), 'banana')
        self.assertEqual(cache.get('c'), 'cherry')
    
    def test_eviction_least_frequently_used(self):
        cache = LFUCache(2)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        cache.get('a')  # Increase frequency of 'a'
        cache.set('c', 'cherry')  # Should evict 'b'
        self.assertIsNone(cache.get('b'), "Least frequently used (b) should be evicted.")
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('c'), 'cherry')
    
    def test_update_value(self):
        cache = LFUCache(2)
        cache.set('a', 'apple')
        cache.set('a', 'avocado')  # Update the value of 'a'
        self.assertEqual(cache.get('a'), 'avocado', "Value of 'a' should be updated to 'avocado'.")

    def test_eviction_with_same_frequency(self):
        cache = LFUCache(2)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        cache.get('a')  # 'a' and 'b' now have the same frequency
        cache.get('b')
        cache.set('c', 'cherry')  # Should evict the least recently used among 'a' and 'b'
        self.assertTrue(cache.get('b') and not cache.get('a'), "Should evict 'a', the less recently used.")

    def test_no_eviction_when_not_full(self):
        cache = LFUCache(3)
        cache.set('a', 'apple')
        cache.get('a')  # Frequency of 'a' is now 2
        cache.set('b', 'banana')  # No eviction necessary
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('b'), 'banana')
        
    
    def test_eviction_when_full_multiple_times(self):
        cache = LFUCache(2)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        cache.get('a')  # 'a' freq = 2
        cache.get('b')  # 'b' freq = 2
        cache.set('c', 'cherry')  # Should evict 'a' or 'b', least recently used among highest frequency
        cache.get('c')
        cache.get('c')
        cache.set('d', 'date')  # Should evict the other of 'a' or 'b' // that's wrong
        self.assertIsNone(cache.get('a') and cache.get('b'), "One of 'a' or 'b' should be evicted.")
        self.assertIn(cache.get('c'), ['cherry'])
        self.assertIn(cache.get('d'), ['date'])

if __name__ == '__main__':
    unittest.main()