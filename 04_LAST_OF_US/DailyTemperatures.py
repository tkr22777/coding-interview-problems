"""
Daily Temperatures

Problem Statement:
Given an array of integers temperatures representing daily temperatures, return an array answer such that 
answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. 
If there is no future day for which this is possible, keep answer[i] == 0.

Examples:
- Input: temperatures = [73,74,75,71,69,72,76,73]
  Output: [1,1,4,2,1,1,0,0]
  Explanation: 
  - Day 0: 73 → wait 1 day to get a warmer temperature (74 on day 1)
  - Day 1: 74 → wait 1 day to get a warmer temperature (75 on day 2)
  - Day 2: 75 → wait 4 days to get a warmer temperature (76 on day 6)
  - Day 3: 71 → wait 2 days to get a warmer temperature (72 on day 5)
  - Day 4: 69 → wait 1 day to get a warmer temperature (72 on day 5)
  - Day 5: 72 → wait 1 day to get a warmer temperature (76 on day 6)
  - Day 6: 76 → no future warmer temperature, so keep 0
  - Day 7: 73 → no future warmer temperature, so keep 0

- Input: temperatures = [30,40,50,60]
  Output: [1,1,1,0]
  Explanation: Each day except the last has a warmer temperature the next day.

- Input: temperatures = [30,60,90]
  Output: [1,1,0]
  Explanation: Each day except the last has a warmer temperature the next day.

Constraints:
- 1 <= temperatures.length <= 10^5
- 30 <= temperatures[i] <= 100
"""

from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    """
    Find the number of days to wait for a warmer temperature.
    
    Args:
        temperatures: List of daily temperatures
        
    Returns:
        A list where each element is the number of days to wait for a warmer temperature
    
    Approach hints:
    - Use a monotonic decreasing stack to efficiently find the next greater element
    - Store indices in the stack rather than actual temperatures
    - Process the array from left to right, updating result as you go
    - Pay attention to how you compute the number of days between indices
    """
    # TODO: Implement your solution here

    result: List[int] = [0] * len(temperatures)
    for i, temp in enumerate(temperatures):
      for j in range(i+1, len(temperatures)):
        if temperatures[j] > temp:
          result[i] = j - i
          break

    return result

# Test cases
def test_daily_temperatures():
    test_cases = [
        {"temperatures": [73,74,75,71,69,72,76,73], "expected": [1,1,4,2,1,1,0,0]},
        {"temperatures": [30,40,50,60], "expected": [1,1,1,0]},
        {"temperatures": [30,60,90], "expected": [1,1,0]},
        {"temperatures": [89,62,70,58,47,47,46,76,100,70], "expected": [8,1,5,4,3,2,1,1,0,0]},
        {"temperatures": [34,80,80,80,34,80,80,80,34,34], "expected": [1,0,0,5,1,0,0,0,0,0]}
    ]
    
    for i, test_case in enumerate(test_cases):
        temperatures = test_case["temperatures"]
        expected = test_case["expected"]
        result = daily_temperatures(temperatures)
        status = "PASSED" if result == expected else f"FAILED (got {result}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_daily_temperatures()
    
    # Example usage
    temperatures = [73,74,75,71,69,72,76,73]
    print(f"Days to wait for a warmer temperature: {daily_temperatures(temperatures)}") 