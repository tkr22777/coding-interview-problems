from typing import List

# https://leetcode.com/problems/candy/

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candy = []
        for i in range(len(ratings)):
            # print(f"i: {i}, val: {ratings[i]}")
            if i > 0 and ratings[i] > ratings[i - 1]:
                candy.append(candy[i - 1] + 1)
            else:
                candy.append(1)

        # print(candy)
        i = len(ratings) - 2
        while i >= 0:
            # print(f"i: {i} val: {val}")
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
            i -= 1
        # print(candy)
        return sum(candy)


s = Solution()
print(s.candy(ratings=[1,0,2]) == 5 ) # c: [2,1,2] 
print(s.candy(ratings=[0,1,2]) == 6) # c: [1,2,3]
print(s.candy(ratings=[1, 2, 2]) == 4) # c: [1,2,1]
print(s.candy(ratings=[0,1,2,1]) == 7) # c: [1,2,3,1]
print(s.candy(ratings=[1,2,1,3,2,1,0]) == 14) # c: [1,2,1,4,3,2,1]
print(s.candy(ratings=[1,2,5,3,2,1,0]) == 18) # c: [1,2,5,4,3,2,1] 
