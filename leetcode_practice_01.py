from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            # print("left:" + str(left))
            # print("right:" + str(right))
            # print("mid:" + str(mid))
            guess = nums[mid]
            if guess == target:
                return mid
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

nums = [ 1, 3, 5, 6, 9, 11 ] 
#      l = 0             r = 5
# first need to understand the return conditions
# 1. if the mid is a match, that's the index to send
# 2. if the mid is not a match but less the target, our index must be before that, increase left
# 3. if the mid is not a match but greater the target, our index must be before that, decrese right
# 4. left and right merged and value is not found, 
#       - current value is less so I must return left + 1
#       - otherwise, value is higher so I must return left, (although we decreases right but and we are out of loop)

s = Solution()
nums = [1,3,5,6] 
target = 5
expected = 2
print("1st case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [1,3,5,6]
target = 2
expected = 1
print("2nd case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [1,3,5,6]
target = 7
expected = 4
print("3nd case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [3,5,6]
target = 2
expected = 0
print("4th case:" + str(expected == s.searchInsert(nums=nums, target=target)))

nums = [3,5,6]
target = 3
expected = 0
print("5th case:" + str(expected == s.searchInsert(nums=nums, target=target)))

'''
Formulation:
1. if found return the index, mid
2. if not found, we want to find the index of the one just bigger than the number
2. if not found, we want to find the index after the just smaller of the number
'''