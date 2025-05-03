from typing import List
import bisect

"""
Problem: Find the Distance Value Between Two Arrays

Given two arrays arr1 and arr2, and a distance value d:
- For each element in arr1, check if there exists any element in arr2 
  where their absolute difference is less than or equal to d
- Return count of elements in arr1 that have absolute difference > d 
  with all elements in arr2

Approach:
- Sort arr2 to enable binary search
- For each value in arr1, use binary search to find closest elements in arr2
- Only need to check elements at insertion point and one before it
- Time: O(n log m) where n = len(arr1), m = len(arr2)
- Space: O(1) excluding input arrays
"""

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        valid_elements = 0
        arr2.sort()  # Sort to enable binary search
        
        for num in arr1:
            # Find where num would be inserted in sorted arr2
            insert_pos = bisect.bisect_left(arr2, num)
            
            # Check if adjacent elements are within distance d
            # first condition is to make sure we are not out of bounds
            # since insert_pos can be equal to len(arr2)
            if insert_pos < len(arr2) and abs(num - arr2[insert_pos]) <= d:
                continue

            # first condition is to make sure we are not out of bounds
            # since insert_pos - 1 can be negative  
            if insert_pos > 0 and abs(num - arr2[insert_pos - 1]) <= d:
                continue
                
            # If we reach here, num is at least d units away from all elements in arr2
            valid_elements += 1
            
        return valid_elements


def test_find_distance_value():
    solution = Solution()
    
    # Test case 1: Basic case with some valid elements
    assert solution.findTheDistanceValue(
        arr1=[4, 5, 8], 
        arr2=[10, 9, 1, 8], 
        d=2
    ) == 2, "Test case 1 failed"
    
    # Test case 2: Negative numbers in arr2
    assert solution.findTheDistanceValue(
        arr1=[1, 4, 2, 3], 
        arr2=[-4, -3, 6, 10, 20, 30], 
        d=3
    ) == 2, "Test case 2 failed"
    
    # Test case 3: Large numbers with mixed signs
    assert solution.findTheDistanceValue(
        arr1=[2, 1, 100, 3], 
        arr2=[-5, -2, 10, -3, 7], 
        d=6
    ) == 1, "Test case 3 failed"
    
    # Test case 4: Single element in arr2 with large distance
    assert solution.findTheDistanceValue(
        arr1=[-3, 2, -5, 7, 1], 
        arr2=[4], 
        d=84
    ) == 0, "Test case 4 failed"
    
    # Test case 5: Small arrays with mixed positions
    assert solution.findTheDistanceValue(
        arr1=[2, 6], 
        arr2=[-10, 9, 2, -1], 
        d=2
    ) == 1, "Test case 5 failed"
    
    print("All test cases passed!")


if __name__ == "__main__":
    test_find_distance_value()