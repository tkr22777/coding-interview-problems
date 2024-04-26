class Solution(object):
    def minimumSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        lowest_from_left = [None for i in range(len(nums))]
#       print(lowest_from_left)

        prev_low = nums[0]
        for i in range(1, len(nums)):
            if prev_low < nums[i]:
                lowest_from_left[i] = prev_low
            
            if nums[i] < prev_low:
                prev_low = nums[i]

#       print(lowest_from_left)


        lowest_from_right = [None for i in range(len(nums))]
#       print(lowest_from_right)

        prev_low = nums[len(nums) - 1]
        for i in range(1, len(nums)):
            index = len(nums) - 1 - i
            if prev_low < nums[index]:
                lowest_from_right[index] = prev_low
            
            if nums[index] < prev_low:
                prev_low = nums[index]
#       print(lowest_from_right)


        lowest = None
        for i in range(1, len(nums) - 1):
            if lowest_from_left[i] is not None and lowest_from_right[i] is not None:
                current_sum = lowest_from_left[i] + lowest_from_right[i] + nums[i]
#               print("current sum:" + str(current_sum))
                if lowest is None:
                    lowest = current_sum
                
                if current_sum < lowest:
                    lowest = current_sum
        
        if lowest is not None:
            return lowest
        else:
            return -1
