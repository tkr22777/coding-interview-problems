from typing import List

# https://leetcode.com/problems/candy/
# 
# Problem Summary:
# You are giving candies to children standing in a line, represented by an array 'ratings'.
# Each child must have at least one candy.
# Children with a higher rating than their adjacent neighbors should get more candies.
# The goal is to minimize the total number of candies you give out while satisfying these conditions.
# 
# Approach:
# 1. First pass: Ensure each child has at least one candy and children with higher ratings than their
#    left neighbor get more candies than that neighbor.
# 2. Second pass (right to left): Ensure children with higher ratings than their right neighbor get
#    more candies than that neighbor, while maintaining the left neighbor property.
# 3. Return the sum of all candies distributed.

class Solution:
    def minimize_candy(self, ratings: List[int]) -> int:
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
            # print(f"i: {i}, rating: {ratings[i]}")
            if ratings[i] > ratings[i + 1]:
                candy[i] = max(candy[i], candy[i + 1] + 1)
            i -= 1
        # print(candy)
        return sum(candy)


s = Solution()
print(s.minimize_candy(ratings=[1,0,2]) == 5 ) # c: [2,1,2] 
print(s.minimize_candy(ratings=[0,1,2]) == 6) # c: [1,2,3]
print(s.minimize_candy(ratings=[1, 2, 2]) == 4) # c: [1,2,1]
print(s.minimize_candy(ratings=[0,1,2,1]) == 7) # c: [1,2,3,1]
print(s.minimize_candy(ratings=[1,2,1,3,2,1,0]) == 14) # c: [1,2,1,4,3,2,1]
print(s.minimize_candy(ratings=[1,2,5,3,2,1,0]) == 18) # c: [1,2,5,4,3,2,1] 
