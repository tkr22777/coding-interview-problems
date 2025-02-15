import unittest
from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        print("instance created")
        self.capacity = capacity
        self.linked_hash_map = OrderedDict()
    
    def set(self, key: str, value: str) -> str :
        if key in self.linked_hash_map:
            self.linked_hash_map.move_to_end(key)
        elif len(self.linked_hash_map) == self.capacity:
            self.linked_hash_map.popitem(last=False)
            # item = self.linked_hash_map.popitem(last=False)
            # print("popped item:" + str(item))
            # print("ordered dict:" + str(self.linked_hash_map))

        self.linked_hash_map[key] = value
        return value

    def get(self, key: str) -> Optional[str] :
        if key in self.linked_hash_map:
            self.linked_hash_map.move_to_end(key)
            return self.linked_hash_map[key]
        else:
            return None

    # returns number of objects currently in the LRU cache
    def get_count(self) -> int:
        return len(self.linked_hash_map)

    def get_capacity(self) -> int:
        return self.size
    
lru = LRUCache(2)
lru.set("a", "1")
lru.set("b", "2")
lru.set("c", "3")
print(None == lru.get("a")) # a should have been purged/reclaimed

lru.set("d", "4")
print(None == lru.get("b")) # b should have been purged/reclaimed

print("3" == lru.get("c")) # c now would becomes most recently used

lru.set("e", "5")
print(None == lru.get("d")) # d should have been purged/reclaimed

class TestLRUCache(unittest.TestCase):
    def test_set_and_get(self):
        cache = LRUCache(2)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('b'), 'banana')

    def test_eviction_rules(self):
        cache = LRUCache(2)
        cache.set('a', 'apple')
        cache.set('b', 'banana')
        cache.get('a')  # 'a' is now recently used
        cache.set('c', 'cherry')  # This should evict 'b'
        self.assertIsNone(cache.get('b'))
        self.assertEqual(cache.get('a'), 'apple')
        self.assertEqual(cache.get('c'), 'cherry')

    def test_overwrite_value(self):
        cache = LRUCache(2)
        cache.set('a', 'apple')
        cache.set('a', 'avocado')  # Overwrite the value for 'a'
        self.assertEqual(cache.get('a'), 'avocado')

    def test_capacity_limit(self):
        cache = LRUCache(1)
        cache.set('a', 'apple')
        cache.set('b', 'banana')  # This should evict 'a'
        self.assertIsNone(cache.get('a'))
        self.assertEqual(cache.get('b'), 'banana')

if __name__ == '__main__':
    unittest.main()