class Solution(object):

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        map = {}

        outputLeft = []
        outputRight = []

        for i in range(0, len(nums)):
            outputLeft.append(1)
            outputRight.append(1)

        for i in range(0, len(nums)):
            prev_index = i - 1;
            if prev_index >= 0:
                outputLeft[i] = outputLeft[prev_index] * nums[prev_index]

            j = len(nums) - 1 - i;
            next_index = j + 1;

            if next_index < len(nums):
                outputRight[j] = outputRight[next_index] * nums[next_index]

        output = []
        for i in range(0, len(nums)):
            output.append(outputLeft[i] * outputRight[i])

        return output

s = Solution()
print(s.productExceptSelf([1, 2, 3]))
