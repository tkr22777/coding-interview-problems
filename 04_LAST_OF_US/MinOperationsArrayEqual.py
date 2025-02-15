from typing import List

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            if nums1 == nums2:
                return 0
            else:
                return -1

        pos = 0
        neg = 0
        for i in range(len(nums1)):
            diff = nums1[i] - nums2[i]
            if diff % k == 0:
                if diff > 0:
                    pos += int(diff / k)
                else:
                    neg += int(diff / k)
            else:
                return -1

        if pos == (- 1 * neg):
            return pos
        else:
            return -1

# Test cases
s = Solution()
print(s.minOperations(nums1=[4, 3, 1, 4], nums2=[1, 3, 7, 1], k=3) == 2)
print(s.minOperations(nums1=[3, 8, 5, 2], nums2=[2, 4, 1, 6], k=1) == -1) 