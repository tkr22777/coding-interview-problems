from typing import List
# https://leetcode.com/problems/replace-words/

class TrieNode:
    def __init__(self) -> None:
        self.next_node = {}
        self.is_word = False

    def addWord(self, word: str) -> None:
        trie = self
        for c in word:
            if c not in trie.next_node:
                trie.next_node[c] = TrieNode()
            trie = trie.next_node[c]
        trie.is_word = True

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()
        for word in dictionary:
            root.addWord(word)

        words = sentence.split()
        out = []
        for word in words:
            root_word = self.get_root_if_exists(root, word)
            out.append(root_word)
        return " ".join(out)

    def get_root_if_exists(self, root: TrieNode, word: str) -> str:
        chars = []
        trie = root
        for c in word:
            if c in trie.next_node:
                trie = trie.next_node[c]
                chars.append(c)
                if trie.is_word:
                    return "".join(chars)
            else:
                return word

# Test cases
s = Solution()
out = s.replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery")
expected = "the cat was rat by the bat"
print(out)
print(out == expected) 

s = Solution()
out = s.replaceWords(["a", "b", "c"], "aadsfasf absbs bbab cadsfafs")
expected = "a a b c"
print(out)
print(out == expected) 
