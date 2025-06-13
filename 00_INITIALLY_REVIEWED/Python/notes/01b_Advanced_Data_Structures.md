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

# LRU Cache implementation
class LRUCache:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

# Iteration from specific key position
od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])

# Find key and iterate from that position to end
def iterate_from_key(ordered_dict, start_key):
    """Iterate from start_key to end - O(n) to find start, O(1) per iteration"""
    found = False
    for key, value in ordered_dict.items():
        if key == start_key:
            found = True
        if found:
            yield key, value

# Find key and iterate from that position to beginning (reverse)
def iterate_from_key_reverse(ordered_dict, start_key):
    """Iterate from start_key to beginning - O(n) to find start, O(1) per iteration"""
    found = False
    for key, value in reversed(ordered_dict.items()):
        if key == start_key:
            found = True
        if found:
            yield key, value

# Examples with od = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
list(iterate_from_key(od, 'c'))                 # [('c', 3), ('d', 4), ('e', 5)]
list(iterate_from_key_reverse(od, 'c'))         # [('c', 3), ('b', 2), ('a', 1)]

# Resume iteration after finding specific item
def resume_after_key(ordered_dict, start_key):
    """Start iteration AFTER the specified key - O(n) to find start"""
    found = False
    for key, value in ordered_dict.items():
        if found:
            yield key, value
        if key == start_key:
            found = True

# Get slice of OrderedDict from key to key
def get_slice(ordered_dict, start_key, end_key):
    """Get items from start_key to end_key (inclusive) - O(n)"""
    result = OrderedDict()
    started = False
    for key, value in ordered_dict.items():
        if key == start_key:
            started = True
        if started:
            result[key] = value
        if key == end_key:
            break
    return result

# Examples
list(resume_after_key(od, 'b'))                 # [('c', 3), ('d', 4), ('e', 5)]
get_slice(od, 'b', 'd')                         # OrderedDict([('b', 2), ('c', 3), ('d', 4)])

# Practical use case: Process items after checkpoint
def process_after_checkpoint(ordered_dict, checkpoint_key):
    """Process all items added after a specific checkpoint"""
    for key, value in resume_after_key(ordered_dict, checkpoint_key):
        print(f"Processing {key}: {value}")

# Use case: Find user and show all users added after them
users = OrderedDict([
    ('user1', 'Alice'), ('user2', 'Bob'), ('user3', 'Charlie'), 
    ('user4', 'Dave'), ('user5', 'Eve')
])

# Show all users added after 'user2'
for user_id, name in resume_after_key(users, 'user2'):
    print(f"{user_id}: {name}")                 # Prints user3: Charlie, user4: Dave, user5: Eve

# Efficient position-based access (if you know the position)
def get_from_position(ordered_dict, start_pos):
    """Get items starting from position - O(start_pos + k) where k is result size"""
    for i, (key, value) in enumerate(ordered_dict.items()):
        if i >= start_pos:
            yield key, value

# Example: Get items from position 2 onwards
list(get_from_position(od, 2))                  # [('c', 3), ('d', 4), ('e', 5)]
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

# Practical use cases
# 1. Autocomplete system
class AutoComplete:
    def __init__(self, words):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
    
    def get_suggestions(self, prefix, max_suggestions=5):
        """Get autocomplete suggestions - O(m + k)"""
        suggestions = self.trie.get_all_words_with_prefix(prefix)
        return suggestions[:max_suggestions]

# 2. Word search in grid
def word_search_trie(board, words):
    """Find all words from list that exist in 2D board - O(M*N*4^L) where L is max word length"""
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    result = set()
    m, n = len(board), len(board[0])
    
    def dfs(i, j, node, path):
        if node.is_end_word:
            result.add(path)
        
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        
        char = board[i][j]
        if char not in node.children:
            return
        
        # Mark as visited
        board[i][j] = '#'
        
        # Explore all 4 directions
        for di, dj in [(0,1), (1,0), (0,-1), (-1,0)]:
            dfs(i + di, j + dj, node.children[char], path + char)
        
        # Backtrack
        board[i][j] = char
    
    for i in range(m):
        for j in range(n):
            dfs(i, j, trie.root, "")
    
    return list(result)

# 3. Longest word with all prefixes
def longest_word_with_prefixes(words):
    """Find longest word where all prefixes are also words - O(N*M)"""
    trie = Trie()
    for word in words:
        trie.insert(word)
    
    def has_all_prefixes(word):
        node = trie.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
            if not node.is_end_word:  # Prefix must be a complete word
                return False
        return True
    
    result = ""
    for word in words:
        if has_all_prefixes(word):
            if len(word) > len(result) or (len(word) == len(result) and word < result):
                result = word
    
    return result

# 4. Replace words (implement dictionary)
def replace_words(dictionary, sentence):
    """Replace words with their shortest root from dictionary - O(N*M + S*M)"""
    trie = Trie()
    for root in dictionary:
        trie.insert(root)
    
    def find_root(word):
        node = trie.root
        for i, char in enumerate(word):
            if char not in node.children:
                return word  # No root found
            node = node.children[char]
            if node.is_end_word:
                return word[:i+1]  # Found shortest root
        return word
    
    words = sentence.split()
    return ' '.join(find_root(word) for word in words)

# Examples
trie = Trie()
words = ["apple", "app", "application", "apply", "banana"]
for word in words:
    trie.insert(word)

trie.search("app")                              # True
trie.search("appl")                             # False
trie.starts_with("app")                         # True
trie.get_all_words_with_prefix("app")           # ['app', 'apple', 'application', 'apply']

# Autocomplete example
autocomplete = AutoComplete(["apple", "application", "apply", "banana", "band"])
autocomplete.get_suggestions("app")             # ['apple', 'application', 'apply']
autocomplete.get_suggestions("ban")             # ['banana', 'band']
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