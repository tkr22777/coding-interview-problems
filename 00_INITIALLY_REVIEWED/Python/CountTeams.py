from typing import List
import bisect

# Problem Summary:
# Count the number of 3-soldier teams where:
# - Either ratings are strictly increasing (rating[i] < rating[j] < rating[k])
# - Or ratings are strictly decreasing (rating[i] > rating[j] > rating[k])
# Where i < j < k, maintaining original positions in the array.

# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        # Track counts of smaller/bigger elements to the left of each position
        smaller = [0] * n
        bigger = [0] * n
        
        # Maintain sorted list of elements seen so far
        sorted_list = []
        
        # First pass: Calculate smaller and bigger counts
        for i in range(n):
            if sorted_list:
                smaller[i] = bisect.bisect_left(sorted_list, rating[i])
                
                # We use bisect_right here because when subtracting from length,
                # it correctly counts elements strictly greater than rating[i]
                bigger[i] = len(sorted_list) - bisect.bisect_right(sorted_list, rating[i])
            
            bisect.insort(sorted_list, rating[i])
        
        total = 0
        # Second pass: Count valid triplets
        for j in range(1, n - 1):
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    # Increasing sequence: add smaller elements to left of j
                    total += smaller[j]
                elif rating[k] < rating[j]:
                    # Decreasing sequence: add bigger elements to left of j
                    total += bigger[j]
        
        return total

s = Solution()
print(s.numTeams([2,5,3,4,1]) == 3)
print(s.numTeams([2,1,3]) == 0)
print(s.numTeams([1,2,3,4]) == 4)
