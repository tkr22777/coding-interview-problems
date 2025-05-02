from typing import List

# Solution for finding ways to split an array into three contiguous non-empty subarrays
# with specific sum constraints, optimized to avoid Time Limit Exceeded

class Solution:

    def waysToSplit_optimized(self, nums: List[int]) -> int:
        # Modulo to avoid overflow, specified in the problem statement
        MOD = 10**9 + 7
        prefix_sums = self.calculate_prefix_sums(nums)
        total_sum = prefix_sums[-1]
        valid_ways = 0

        # For each potential leftmost subarray
        for left_end in range(len(nums) - 2):
            # Sum of leftmost subarray
            left_sum = prefix_sums[left_end]
            
            # Early termination: if left sum is greater than a third of total sum,
            # no valid splits are possible from this point on
            if left_sum * 3 > total_sum:
                break

            # First binary search: find the starting index of middle array where first condition is valid
            min_middle = left_end + 1
            max_middle = len(nums) - 2

            # the following figues out the starting index of the middle subarray
            while min_middle <= max_middle:
                mid_middle = min_middle + (max_middle - min_middle) // 2
                middle_sum = prefix_sums[mid_middle] - left_sum

                if left_sum > middle_sum:
                    min_middle = mid_middle + 1
                else:
                    max_middle = mid_middle - 1
            
            # Smallest index where left_sum <= middle_sum
            # Since it is a non-negative array, the first
            # condition is valid starting from min_middle
            min_valid_middle = min_middle

            # Second binary search: 
            # find the largest index of the middle subarray
            # where the second condition is valid
            min_middle = min_valid_middle
            max_middle = len(nums) - 2
            
            while min_middle <= max_middle:
                mid_middle = min_middle + (max_middle - min_middle) // 2
                middle_sum = prefix_sums[mid_middle] - left_sum
                right_sum = total_sum - prefix_sums[mid_middle]

                if middle_sum > right_sum:
                    max_middle = mid_middle - 1
                else:
                    min_middle = mid_middle + 1
            
            # Largest index where middle_sum <= right_sum after the min_valid_middle
            max_valid_middle = max_middle
            
            # Count all valid middle subarrays for this left subarray
            if max_valid_middle >= min_valid_middle:
                valid_ways = (valid_ways + (max_valid_middle - min_valid_middle + 1)) % MOD
                
        return valid_ways

    def waysToSplit_brute_force(self, nums: List[int]) -> int:
        prefix_sums = self.calculate_prefix_sums(nums)
        total_sum = prefix_sums[-1]
        valid_ways = 0
        
        # For each potential leftmost subarray
        for left_end in range(len(nums) - 2):
            left_sum = prefix_sums[left_end]

            # For each potential middle subarray
            for middle_end in range(left_end + 1, len(nums) - 1):
                middle_sum = prefix_sums[middle_end] - left_sum
                right_sum = total_sum - prefix_sums[middle_end]

                
                # Check if the split is valid
                if left_sum <= middle_sum and middle_sum <= right_sum:
                    valid_ways += 1
                # Early termination: if middle sum > right sum, all subsequent splits will be invalid
                # left_sum > middle_sum should not break since we want to try the next element
                elif middle_sum > right_sum:
                    break
                    
        return valid_ways

    def calculate_prefix_sums(self, nums: List[int]) -> List[int]:
        """
        Calculate prefix sums for an array.
        prefix_sums[i] represents the sum of elements from 0 to i (inclusive).
        """
        prefix_sums = [0] * len(nums)
        for i in range(len(nums)):
            prefix_sums[i] = nums[i]
            if i > 0:
                prefix_sums[i] += prefix_sums[i-1]
        return prefix_sums

# Test cases
s = Solution()

print(s.waysToSplit_brute_force([1,1,1]) == 1)
print(s.waysToSplit_brute_force([1,2,2,2,5,0]) == 3)
print(s.waysToSplit_brute_force([3,2,1]) == 0)

print(s.waysToSplit_optimized([1,1,1]) == 1)
print(s.waysToSplit_optimized([1,2,2,2,5,0]) == 3)
print(s.waysToSplit_optimized([3,2,1]) == 0)
