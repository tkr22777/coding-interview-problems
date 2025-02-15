from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = []
        for i in range(len(ratings)):
            if i > 0 and ratings[i] > ratings[i - 1]:
                candy.append(candy[i - 1] + 1)
            else:
                candy.append(1)

        i = len(ratings) - 2
        while i >= 0:
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
            i -= 1
        return sum(candy)

# Test cases
s = Solution()
print(s.candy(ratings=[1,0,2]))
print(s.candy(ratings=[0,1,2]))
print(s.candy(ratings=[1, 2, 2])) 