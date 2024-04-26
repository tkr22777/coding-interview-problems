# https://leetcode.com/problems/find-and-replace-in-string/description/
import heapq
from typing import List

class Solution:
    def findReplaceString(self, input: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        candidates = []
        for i in range(len(indices)):
            index = indices[i]
            source = sources[i]
            # print("index: " + str(index) + ", cs: " + current_str)
            if input[index: index + len(source)] == source:
                heapq.heappush(candidates, (index, i))
        
        current_str = input
        offset = 0
        while len(candidates) > 0:
            index, i = heapq.heappop(candidates)
            index = index + offset
            source = sources[i]
            source_len = len(source)
            if current_str[index: index + source_len] == source:
                current_str = current_str[:index] + targets[i] + current_str[index + source_len:]
                offset += (len(targets[i]) - source_len)

        # print(current_str)
        return current_str

s = Solution()

input = "abcd"
indices = [0, 2]
sources = ["a", "cd"]
targets = ["eee", "ffff"]

print("1st case:" + str("eeebffff" == s.findReplaceString(input, indices, sources, targets)))

input = "abcd"
indices = [0, 2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
print("2nd case:" + str("eeecd" == s.findReplaceString(input, indices, sources, targets)))

input = "vmokgggqzp"
indices = [3,5,1]
sources = ["kg","ggq","mo"]
targets = ["s","so","bfr"]
print("3rd case:" + str("vbfrssozp" == s.findReplaceString(input, indices, sources, targets)))