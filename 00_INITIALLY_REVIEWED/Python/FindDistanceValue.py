from typing import List
import bisect

# Problem: Find the Distance Value Between Two Arrays
# Count elements in arr1 where for every element in arr2, 
# the absolute difference is strictly greater than d.
# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        arr2.sort()
        
        for v1 in arr1:
            # Find index where v1 would be inserted in arr2
            i = bisect.bisect_left(arr2, v1)
            
            # Check if elements at positions i and i-1 are within distance d
            if i < len(arr2) and abs(v1 - arr2[i]) <= d:
                continue
                
            if i > 0 and abs(v1 - arr2[i-1]) <= d:
                continue
                
            # If we get here, v1 is at least d units away from all elements in arr2
            count += 1
            
        return count

s = Solution()

print(s.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2) == 2)
print(s.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3) == 2)
print(s.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6) == 1)
print(s.findTheDistanceValue(arr1=[-3, 2, -5, 7, 1], arr2=[4], d=84) == 0)
print(s.findTheDistanceValue(arr1=[2, 6], arr2=[-10, 9, 2, -1], d=2) == 1)