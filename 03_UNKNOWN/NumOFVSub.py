
class Solution(object):

    def validSubarrays(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        print nums
        resultsMap = {}
        subArrays = 0

        for start in range(len(nums)):
            for end in range(start, len(nums)):
                if start == end:
                    subArrays += 1
                elif nums[start] <= nums[end]:
                    subArrays += 1
                else:
                    break
        return subArrays

print Solution().validSubarrays([1, 4, 2, 5, 3])



