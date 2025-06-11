"""
Permutation Sequence

Problem Statement:
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.
By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the kth permutation sequence.

Examples:
- Input: n = 3, k = 3
  Output: "213"
  Explanation: The sequence contains 6 permutations. The 3rd one is "213".

- Input: n = 4, k = 9
  Output: "2314"
  Explanation: The sequence contains 24 permutations. The 9th one is "2314".

- Input: n = 3, k = 1
  Output: "123"
  Explanation: The first permutation is the sorted sequence.

Constraints:
- 1 <= n <= 9
- 1 <= k <= n!
"""

def get_permutation(n: int, position: int) -> str:
    """
    Find the kth permutation sequence of numbers 1 to n.
    
    Args:
        n: The size of the set (1 to n)
        position: The position of the required permutation sequence (1-indexed)
        
    Returns:
        The permutation sequence at the specified position as a string
    
    Approach hints:
    - Computing all permutations would be inefficient
    - Consider using factorials to determine the position of each digit
    - Think of dividing the permutation space into blocks based on the first digit, then recursively 
      finding the correct block and digit
    - This can be solved using the factorial number system (or factoradic) representation of the position
    """
    # TODO: Implement your solution here
    pass


# Helper function to calculate factorial
def factorial(n: int) -> int:
    """Calculate the factorial of n."""
    # TODO: Implement factorial calculation
    pass


# Test cases
def test_get_permutation():
    test_cases = [
        {"n": 3, "position": 3, "expected": "213"},
        {"n": 4, "position": 9, "expected": "2314"},
        {"n": 3, "position": 1, "expected": "123"},
        {"n": 2, "position": 2, "expected": "21"},
        {"n": 9, "position": 278811, "expected": "752861349"}
    ]
    
    for i, test_case in enumerate(test_cases):
        n = test_case["n"]
        position = test_case["position"]
        expected = test_case["expected"]
        result = get_permutation(n, position)
        status = "PASSED" if result == expected else f"FAILED (got '{result}', expected '{expected}')"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_get_permutation()
    
    # Example usage
    n, position = 3, 3
    print(f"The {position}th permutation of {n} numbers is: {get_permutation(n, position)}") 