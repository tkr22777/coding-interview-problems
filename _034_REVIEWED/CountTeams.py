from typing import List
import bisect

# https://leetcode.com/problems/count-number-of-teams/

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        # For each index i, store count of:
        # smaller[i] = numbers smaller than rating[i] to its left
        # bigger[i] = numbers bigger than rating[i] to its left
        smaller = [0] * n
        bigger = [0] * n
        
        # Use sorted_list to keep track of all elements to the left
        sorted_list = []
        
        # First pass: Calculate smaller and bigger counts for each position
        for i in range(n):
            if sorted_list:
                # Count elements smaller than current element
                smaller[i] = bisect.bisect_left(sorted_list, rating[i])
                # Count elements bigger than current element
                bigger[i] = len(sorted_list) - bisect.bisect_right(sorted_list, rating[i])
            
            # Add current element to sorted list for next iterations
            bisect.insort(sorted_list, rating[i])
        
        total = 0
        # Second pass: Count valid triplets
        # For each middle element (j), look at elements to its right (k)
        for j in range(1, n - 1):
            for k in range(j + 1, n):
                if rating[k] > rating[j]:
                    # For increasing sequence (i < j < k):
                    # Add count of elements smaller than rating[j] to its left
                    total += smaller[j]
                elif rating[k] < rating[j]:
                    # For decreasing sequence (i > j > k):
                    # Add count of elements bigger than rating[j] to its left
                    total += bigger[j]
        
        return total

s = Solution()
print(s.numTeams([2,5,3,4,1]) == 3)
print(s.numTeams([2,1,3]) == 0)
print(s.numTeams([1,2,3,4]) == 4)
