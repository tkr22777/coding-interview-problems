# Advanced Data Structures

<details>
<summary><strong>OrderedDict Utilities</strong></summary>

```python
# Time Complexity:
# - Access/Insert/Delete: O(1) average case
# - move_to_end: O(1)
# - popitem: O(1)
# Space Complexity: O(n)

from collections import OrderedDict

od = OrderedDict()
od['a'] = 1                                     # O(1)
od['b'] = 2                                     # O(1)
od['c'] = 3                                     # O(1)

# Access and modify
value = od['a']                                 # O(1)
od['a'] = 4                                     # O(1)
size = len(od)                                  # O(1)

# Check membership
if 'a' in od:                                   # O(1)
    od['a'] = 6                                 # O(1)

# Move elements
od.move_to_end('a')                             # O(1)
od.move_to_end('b', last=False)                 # O(1)

# Pop operations
key, value = od.popitem()                       # O(1)
key, value = od.popitem(last=False)             # O(1)

# Peek operations
key, value = next(iter(od.items()))             # O(1)
key, value = next(reversed(od.items()))         # O(1)

# Clear
od.clear()                                      # O(1)

# LRU Cache implementation (main use case)
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)  # Mark as recently used
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)  # Remove least recently used

# ❌ NO built-in "jump to key" iteration - always O(n) scan from start
# ✅ If you need this pattern, consider using index-based data structure instead
```

</details>

<details>
<summary><strong>Trie (Prefix Tree)</strong></summary>

```python
# Time Complexity:
# - Insert: O(m) where m is length of word
# - Search: O(m) where m is length of word
# - StartsWith: O(m) where m is length of prefix
# Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words, M is average length

class TrieNode:
    def __init__(self):
        self.children = {}  # char -> TrieNode
        self.is_end_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """Insert word into trie - O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_word = True
    
    def search(self, word):
        """Search for exact word - O(m)"""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_word
    
    def starts_with(self, prefix):
        """Check if any word starts with prefix - O(m)"""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def get_all_words_with_prefix(self, prefix):
        """Get all words that start with prefix - O(m + k) where k is result size"""
        node = self.root
        # Navigate to prefix end
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        
        # DFS to collect all words from this node
        result = []
        self._dfs_collect_words(node, prefix, result)
        return result
    
    def _dfs_collect_words(self, node, current_word, result):
        """Helper for collecting all words from a node"""
        if node.is_end_word:
            result.append(current_word)
        
        for char, child_node in node.children.items():
            self._dfs_collect_words(child_node, current_word + char, result)

# Main use case: Autocomplete/Prefix search
trie = Trie()
words = ["apple", "app", "apply"]
for word in words:
    trie.insert(word)

trie.search("app")                              # True
trie.starts_with("app")                         # True  
trie.get_all_words_with_prefix("app")           # ['app', 'apple', 'apply']
```

</details>

<details>
<summary><strong>LinkedList</strong></summary>

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Basic operations
def append(head, val):
    if not head:
        return ListNode(val)
    curr = head
    while curr.next:
        curr = curr.next
    curr.next = ListNode(val)
    return head

def prepend(head, val):
    return ListNode(val, head)

def delete(head, val):
    if not head:
        return None
    if head.val == val:
        return head.next
    curr = head
    while curr.next:
        if curr.next.val == val:
            curr.next = curr.next.next
            break
        curr = curr.next
    return head

# Common patterns
def reverse(head):
    prev = None
    curr = head
    while curr:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def merge_two_sorted(l1, l2):
    dummy = ListNode(0)
    curr = dummy
    
    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    
    curr.next = l1 or l2
    return dummy.next

def remove_nth_from_end(head, n):
    dummy = ListNode(0)
    dummy.next = head
    first = second = dummy
    
    # Move first n+1 steps ahead
    for _ in range(n + 1):
        first = first.next
    
    # Move both until first reaches end
    while first:
        first = first.next
        second = second.next
    
    # Remove the nth node from end
    second.next = second.next.next
    return dummy.next
```

</details> 