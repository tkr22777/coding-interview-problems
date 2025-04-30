from collections import OrderedDict
from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.linked_hash_map = OrderedDict()

    def set(self, key: str, value: str) -> str :
        if key in self.linked_hash_map:
            self.linked_hash_map.move_to_end(key)
        elif len(self.linked_hash_map) == self.capacity:
            self.linked_hash_map.popitem(last=False)

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
        return self.capacity

lru = LRUCache(2)
lru.set("a", "1")
lru.set("b", "2")
lru.set("c", "3")
print(lru.get("a") is None) # a should have been purged/reclaimed
lru.set("d", "4")
print(lru.get("b") is None) # b should have been purged/reclaimed
print(lru.get("c") == "3")  # c now would becomes most recently used
lru.set("e", "5")
print(lru.get("d") is None) # d should have been purged/reclaimed
