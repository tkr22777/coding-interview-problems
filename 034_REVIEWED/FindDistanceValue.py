from typing import List
import bisect

# https://leetcode.com/problems/find-the-distance-value-between-two-arrays/description/

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:

        count = 0
        arr2.sort()
        # print(arr2)
        for v1 in arr1:
            i = bisect.bisect_left(arr2, v1)

            # the value at i should be either bigger, equal 
            # or i is at len(arr2) (all values are smaller than v1)
            if (i < len(arr2) and 
                int(abs(v1 - arr2[i])) <= d):
                continue
            # print("v1: " + str(v1) + " i:"+ str(i))

            if (i - 1 >= 0 and 
                i - 1 < len(arr2) and 
                int(abs(v1 - arr2[i - 1])) <= d):
                continue
            # print("v1: " + str(v1) + " i:"+ str(i))

            count += 1

        # print("count:" + str(count))
        return count

s = Solution()

print(s.findTheDistanceValue(arr1=[4, 5, 8], arr2=[10, 9, 1, 8], d=2) == 2)
print(s.findTheDistanceValue(arr1=[1, 4, 2, 3], arr2=[-4, -3, 6, 10, 20, 30], d=3) == 2)
print(s.findTheDistanceValue(arr1=[2, 1, 100, 3], arr2=[-5, -2, 10, -3, 7], d=6) == 1)
print(s.findTheDistanceValue(arr1=[-3, 2, -5, 7, 1], arr2=[4], d=84) == 0)
print(s.findTheDistanceValue(arr1=[2, 6], arr2=[-10, 9, 2, -1], d=2) == 1)