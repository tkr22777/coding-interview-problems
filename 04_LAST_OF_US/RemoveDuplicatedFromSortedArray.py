"""
Problem Statement:
Given a sorted array of integers, remove the duplicates in-place such that each element
appears only once and returns the new length.

Do not allocate extra space for another array; you must do this by modifying the input
array in-place with O(1) extra memory.

Example:
Input: nums = [1, 1, 2]
Output: 2, nums = [1, 2, _]
Explanation: Your function should return length = 2, with the first two elements
of nums being 1 and 2 respectively. It doesn't matter what you leave beyond the returned length.

Input: nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
Explanation: Your function should return length = 5, with the first five elements
of nums being modified to 0, 1, 2, 3, and 4 respectively. It doesn't matter what values
are set beyond the returned length.

Constraints:
- 0 <= nums.length <= 3 * 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in ascending order
"""

def remove_duplicates(nums):
    """
    Remove duplicates from sorted array in-place.
    
    Args:
        nums: List[int] - A sorted array of integers
        
    Returns:
        int - The new length of the array with duplicates removed
        
    Note:
        The input array should be modified in-place, with the unique elements
        at the beginning of the array, and the length returned.
    """
    # Handle empty array case
    if not nums:
        return 0
    
    # Use two pointers: i is the position to place the next unique element
    # j scans through the array
    i = 0  # Position to place the next unique element
    
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    # Return the length of the unique part (i + 1)
    return i + 1

# Test cases
def test_remove_duplicates():
    # Test Case 1: Basic case with a few duplicates
    nums1 = [1, 1, 2]
    expected_length1 = 2
    expected_array1 = [1, 2]
    
    # Test Case 2: More complex case with multiple duplicates
    nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    expected_length2 = 5
    expected_array2 = [0, 1, 2, 3, 4]
    
    # Test Case 3: No duplicates
    nums3 = [1, 2, 3, 4, 5]
    expected_length3 = 5
    expected_array3 = [1, 2, 3, 4, 5]
    
    # Test Case 4: All elements are the same
    nums4 = [1, 1, 1, 1, 1]
    expected_length4 = 1
    expected_array4 = [1]
    
    # Test Case 5: Empty array
    nums5 = []
    expected_length5 = 0
    expected_array5 = []
    
    # Run tests
    test_cases = [
        (nums1, expected_length1, expected_array1),
        (nums2, expected_length2, expected_array2),
        (nums3, expected_length3, expected_array3),
        (nums4, expected_length4, expected_array4),
        (nums5, expected_length5, expected_array5)
    ]
    
    all_passed = True
    print("Running tests...")
    
    for i, (nums, expected_length, expected_array) in enumerate(test_cases, 1):
        # Create a copy to display the original input
        original_nums = nums.copy()
        
        # Call the function
        result_length = remove_duplicates(nums)
        
        # Verify the length returned
        length_correct = result_length == expected_length
        
        # Verify the modified array (only check the elements up to the returned length)
        array_correct = True
        for j in range(min(result_length, len(expected_array))):
            if j >= len(nums) or nums[j] != expected_array[j]:
                array_correct = False
                break
        
        # Display simplified results
        test_passed = length_correct and array_correct
        all_passed = all_passed and test_passed
        
        print(f"Test {i}: {original_nums} -> {nums[:result_length]} (Length: {result_length}) - {'PASS' if test_passed else 'FAIL'}")
        
        # Only show details for failed tests
        if not test_passed:
            print(f"  Expected Length: {expected_length}, Got: {result_length}")
            print(f"  Expected Array: {expected_array}")
            print(f"  Modified Array: {nums[:result_length]}")
    
    print(f"\nOverall: {'ALL TESTS PASSED!' if all_passed else 'SOME TESTS FAILED!'}")


if __name__ == "__main__":
    test_remove_duplicates()
    
    # You can add your own test cases here
    # Example:
    # my_array = [1, 1, 2, 3, 3, 4, 5, 5]
    # length = remove_duplicates(my_array)
    # print(f"Length: {length}, Array: {my_array[:length]}")
