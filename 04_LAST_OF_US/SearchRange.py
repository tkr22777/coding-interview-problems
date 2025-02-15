from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if not nums or len(nums) == 0:
            return [-1, -1]

        def start_index(nums, target):
            left = 0
            right = len(nums) - 1

            # left equals to right is a candidate since, when left and right are equal,
            # the set with single element, where the set condition maybe is satisfied
            while left <= right:
                mid = int((left + right) / 2)  # 1
                # the set satisfying condition
                if nums[mid] == target:
                    if mid - 1 >= 0:  # there might be more on the left
                        if nums[mid - 1] < nums[mid]:  # there's no more left to go
                            return mid
                        else:  # we can go further left and thus right is curved
                            right = mid - 1
                    else:  # the mid is the first and candidate element
                        return mid
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        def end_index(nums, start):
            val = nums[start]

            while start < len(nums) and val == nums[start]:
                start += 1

            return start - 1

        start = start_index(nums, target)

        if start == -1:
            return [-1, -1]

        end = end_index(nums, start)
        return [start, end]

    # a solution from leetcode
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binsearch(nums, target, True)
        right = self.binsearch(nums, target, False)
        return [left, right]

    def binsearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i

# Test cases
s = Solution()
nums = [5, 7, 7, 8, 8, 10]
target = 8
expected = [3, 4]
print("1st case:" + str(expected == s.searchRange(nums=nums, target=target)))

nums = [5, 7, 7, 8, 8, 10]
target = 6
expected = [-1, -1]
print("2nd case:" + str(expected == s.searchRange(nums=nums, target=target)))

nums = []
target = 0
expected = [-1, -1]
print("3rd case:" + str(expected == s.searchRange(nums=nums, target=target))) 


nums = [5, 7, 7, 8, 10]
target = 8
expected = [3, 3]
out = s.searchRange(nums=nums, target=target)
print("4th case:" + str(expected == out))

nums = [7, 8, 8, 10, 11]
target = 7
expected = [0, 0]
out = s.searchRange(nums=nums, target=target)
print("5th case:" + str(expected == out))

nums = [7, 8, 8, 10, 11]
target = 11
expected = [4, 4]
out = s.searchRange(nums=nums, target=target)
print("6th case:" + str(expected == out))

nums = [7, 8, 8, 10, 11, 11, 11, 11]
target = 11
expected = [4, 7]
out = s.searchRange(nums=nums, target=target)
print("7th case:" + str(expected == out))

nums = [1, 1, 2]
target = 1
expected = [0, 1]
out = s.searchRange(nums=nums, target=target)
print("8th case:" + str(expected == out))