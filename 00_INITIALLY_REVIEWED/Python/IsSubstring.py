"""
Is Substring (Prefix) Checker
Check if a string is a prefix of any word in a list using a Trie data structure.
Example: ["america", "art"] -> "am" is True, "at" is False
"""
from typing import List

class Trie:
    def __init__(self):
        self.next = {}
        self.complete = False

    def add_word(self, word: str):
        if word or len(word) > 0:
            node = self
            for chr in word:
                if chr in node.next:
                    node = node.next[chr]
                else:
                    node.next[chr] = Trie()
                    node = node.next[chr]
            node.complete = True

    def is_substring(self, word: str) -> bool:
        node = self
        for ch in word:
            if ch in node.next:
                node = node.next[ch]
            else:
                return False
        return True


class Solution:
    def is_substring(self, words: List[str], word: str) -> bool:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        return trie.is_substring(word)


def test_is_substring():
    s = Solution()
    
    test_cases = [
        (["america", "art", "banana", "cuteness", "aweful"], "awe", True),    # Found prefix
        (["america", "art", "banana", "cuteness", "aweful"], "darn", False),  # Not found
        (["america", "art", "banana", "cuteness", "aweful"], "ban", True),    # Another match
        (["america", "art", "banana", "cuteness", "aweful"], "banu", False),  # Partial match
        (["america", "art", "banana", "cuteness", "aweful"], "cut", True),    # Beginning of word
        ([], "anything", False),                                              # Empty list
        (["a"], "a", True),                                                   # Exact match
    ]
    
    for words, query, expected in test_cases:
        result = s.is_substring(words, query)
        assert result == expected, f"For query '{query}' in {words}: expected {expected}"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_is_substring()
