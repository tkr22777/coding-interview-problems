"""
Subarray Sum Equals K

Find the total number of continuous subarrays in an array whose sum equals k.

Examples:
- nums = [1,1,1], k = 2 -> 2 (subarrays [1,1] at different positions)
- nums = [1,2,3], k = 3 -> 2 (subarrays [1,2] and [3])

Constraints:
- 1 <= nums.length <= 2 * 10^4
- -1000 <= nums[i] <= 1000
- -10^7 <= k <= 10^7
"""

from typing import List
import bisect

def subarray_sum(nums: List[int], k: int) -> int:
    """
    Find the number of continuous subarrays whose sum equals k.
    """
    
    prefix_sum_index = {}
    prefix_sum = 0
    prefix_sum_array = [0] * len(nums)

    for i in range(len(nums)):
        # print(f"i: {i}, nums[i]: {nums[i]}")
        prefix_sum += nums[i]
        prefix_sum_array[i] = prefix_sum

        sorted_indices = prefix_sum_index.get(prefix_sum, [])
        bisect.insort(sorted_indices, i)
        prefix_sum_index[prefix_sum] = sorted_indices

    # print(prefix_sum_index)

    count = 0
    for i, prefix_sum in enumerate(prefix_sum_array):
        if prefix_sum == k:
            count += 1

        sorted_indices = prefix_sum_index.get(prefix_sum + k, [])
        # print(f"i: {i}, prefix_sum: {prefix_sum}, count: {count}, iset: {sorted_indices}")
        count += len(sorted_indices) - bisect.bisect_right(sorted_indices, i)
    return count

def test_subarray_sum():
    test_cases = [
        {"nums": [1,1,1], "k": 2, "expected": 2},
        {"nums": [1,2,3], "k": 3, "expected": 2},
        {"nums": [1], "k": 0, "expected": 0},
        {"nums": [1,-1,0], "k": 0, "expected": 3},
        {"nums": [3,4,7,2,-3,1,4,2], "k": 7, "expected": 4},
        {"nums": [1,2,1,2,1], "k": 3, "expected": 4}
    ]
    
    for i, test in enumerate(test_cases):
        result = subarray_sum(test["nums"], test["k"])
        status = "PASSED" if result == test["expected"] else f"FAILED (got {result}, expected {test['expected']})"
        print(f"Test {i+1}: {status}")

if __name__ == "__main__":
    test_subarray_sum()
