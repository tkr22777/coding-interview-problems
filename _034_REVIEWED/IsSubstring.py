from typing import List

class Trie:
    def __init__(self):
        self.next = {}
        self.complete = False

    def add_word(self, word: str):
        if word or len(word) > 0:
            node = self
            for chr in word:
                # for key in node.next.keys():
                #     print("word:" + str(word) + " key:" + key)
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


class Main:
    def is_substring(self, words: List[str], word: str) -> bool:
        trie = Trie()
        for w in words:
            trie.add_word(w)
        return trie.is_substring(word)

m = Main()
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "darn") == False)
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "awe") == True)
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "ban") == True)
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "banu") == False)
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "donky") == False)
print(m.is_substring(["america", "art", "banana", "cuteness", "aweful"], "cut") == True)
