
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
#
class Solution0:

    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l = 0
        r = len(letters) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) <= ord(target):
                l = mid + 1
            else:
                r = mid - 1

        if l >= len(letters):
            return letters[0]
        else:
            return letters[l]

# https://leetcode.com/problems/count-binary-substrings/
class Solution1:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) == 0 or len(s) == 1:
            return 0

        prev = s[0]
        if prev == '1':
            one_candidate = 1
            zero_candidate = 0
        else:
            one_candidate = 0
            zero_candidate = 1
        
        total = 0
        for bin in s[1:]:
            if bin == '1':
                if prev == '0':
                    total += min(zero_candidate, one_candidate)
                    one_candidate = 1
                else:
                    one_candidate += 1
            else:
                if prev == '1':
                    total += min(zero_candidate, one_candidate)
                    zero_candidate = 1
                else:
                    zero_candidate += 1
            prev = bin
        total += min(zero_candidate, one_candidate)
        return total

s = Solution1()
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("00110011"))
print(s.countBinarySubstrings("11000"))
print(s.countBinarySubstrings("0011"))
print(s.countBinarySubstrings("001110000"))
print(s.countBinarySubstrings("001101"))
print(s.countBinarySubstrings("101"))

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

class Solution2:
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

out = s.replaceWords(["cat","bat","rat"], "the cattle was rattled by the battery")
expected = "the cat was rat by the bat"
print(out)
print(out == expected)



from typing import List
class Solution3:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)
        intersection = set_nums1.intersection(set_nums2)
        
        if len(intersection) > 0:
            min_common = intersection.pop()
            while len(intersection) > 0:
                current = intersection.pop()
                min_common = min(min_common, current)
            return min_common
        
        first_min = nums1[0]
        for num in nums1[1:]:
            first_min = min(first_min, num)

        second_min = nums2[0]
        for num in nums2[1:]:
            second_min = min(second_min, num)

        if first_min < second_min:
            return second_min + first_min  * 10
        else:
            return first_min + second_min * 10


s = Solution3()
print(s.minNumber([4,1,3], [5,7]))
print(s.minNumber([4,1,2,3], [5, 2,7]))
print(s.minNumber([4,3], [5,1,7]))

#https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/
class Solution4:
    def minimumLength(self, s: str) -> int:
        i = 0
        j = len(s) - 1
        while i < len(s) - 1 and j >= 0 and s[i] == s[j]:
            while i < len(s) - 1 and s[i] == s[i + 1] and i + 1 < j:
                i += 1

            while j >= 0 and s[j] == s[j - 1] and i < j - 1:
                j -= 1

            i += 1
            j -= 1
            if i == j:
                return 1
            if i > j:
                return 0

        return j - i + 1
        
s = Solution4()
print(2 == s.minimumLength("ca"))
print(1 == s.minimumLength("cac"))
print(0 == s.minimumLength("cabaabac"))
print(3 == s.minimumLength("aabccabba"))
print(1 == s.minimumLength("c"))