class Solution:
    def product_except_self(self, nums):
        """
        Calculate the product of all elements in the array except self at each position.
        
        For each element at index i, calculate the product of all elements except nums[i].
        """

        # Initialize arrays to store cumulative products
        array_length = len(nums)
        left_products = [1] * array_length
        right_products = [1] * array_length
        
        # Calculate cumulative products from left to right
        for i in range(array_length):
            previous_index = i - 1
            if previous_index >= 0:
                left_products[i] = left_products[previous_index] * nums[previous_index]
            
            # Calculate cumulative products from right to left
            right_index = array_length - 1 - i
            next_index = right_index + 1
            
            if next_index < array_length:
                right_products[right_index] = right_products[next_index] * nums[next_index]
        
        # Combine left and right products to get the final result
        result = []
        for i in range(array_length):
            result.append(left_products[i] * right_products[i])
            
        return result


def test_product_except_self():
    """Test the product_except_self function with individual assertions."""
    s = Solution()
    assert s.product_except_self([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert s.product_except_self([0, 1, 2, 3]) == [6, 0, 0, 0]
    assert s.product_except_self([0, 0, 2, 3]) == [0, 0, 0, 0]
    assert s.product_except_self([-1, -2, -3, -4]) == [-24, -12, -8, -6]
    assert s.product_except_self([5]) == [1]
    assert s.product_except_self([1, 2, 3]) == [6, 3, 2]
    print("All tests passed!")


# Run the tests
if __name__ == "__main__":
    test_product_except_self()
