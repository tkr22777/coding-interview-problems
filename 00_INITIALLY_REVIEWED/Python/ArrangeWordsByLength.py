import heapq

# https://leetcode.com/problems/rearrange-words-in-a-sentence/

class Solution:
    def arrangeWords(self, text: str) -> str:
        heap = []
        words = text.split()
        for i in range(len(words)):
            heapq.heappush(heap, (len(words[i]), i))

        out = ""
        _, i = heapq.heappop(heap)
        out += words[i].capitalize()
        while len(heap) > 0:
            _, i = heapq.heappop(heap)
            out += " " + words[i].lower()
        return out


s = Solution()
print(s.arrangeWords("Leetcode is cool") == "Is cool leetcode")
print(s.arrangeWords("Keep calm and code on") == "On and keep calm code")