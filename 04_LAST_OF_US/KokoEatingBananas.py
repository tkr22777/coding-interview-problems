"""
Koko Eating Bananas

Given piles of bananas and hours h, find minimum eating speed k to finish all bananas in h hours.
Each hour Koko eats k bananas from one pile (or all if pile < k).

Examples:
- piles = [3,6,7,11], h = 8 -> k = 4
- piles = [30,11,23,4,20], h = 5 -> k = 30
- piles = [30,11,23,4,20], h = 6 -> k = 23

Constraints:
- 1 <= piles.length <= 10^4
- piles.length <= h <= 10^9
- 1 <= piles[i] <= 10^9
"""

from typing import List
import math

def min_eating_speed(piles: List[int], hours_available: int) -> int:
    """Find minimum eating speed to finish all bananas within h hours."""
    if hours_available < len(piles):
        return -1

    if hours_available == len(piles):
        return max(piles)

    left = 1
    right = max(piles) #  O(n)

    while left < right:
        mid = left + (right - left) // 2
        hours = hours_needed(piles, mid)
        # print(f"left: {left}, right: {right}, mid: {mid}, hours: {hours}")
        if hours > hours_available:
            left = mid + 1
        else:
            right = mid

    return left
   
# Helper function to calculate hours needed to eat all piles at a given speed
def hours_needed(piles: List[int], speed: int) -> int: # O(n)

    hours = 0
    for i in range(len(piles)):
        hours += math.ceil(piles[i] / speed)
        
    print(f"speed: {speed}, hours: {hours}")
    return hours

# Test cases
def test_min_eating_speed():
    test_cases = [
        {"piles": [3,6,7,11], "hours_available": 8, "expected": 4},
        {"piles": [30,11,23,4,20], "hours_available": 5, "expected": 30},
        {"piles": [30,11,23,4,20], "hours_available": 6, "expected": 23},
        {"piles": [312884470], "hours_available": 312884469, "expected": 2},
        {"piles": [1,1,1,999999999], "hours_available": 10, "expected": 142857143}
    ]
    
    for i, test in enumerate(test_cases):
        result = min_eating_speed(test["piles"], test["hours_available"])
        status = "PASSED" if result == test["expected"] else f"FAILED (got {result}, expected {test['expected']})"
        print(f"Test {i+1}: {status}")

if __name__ == "__main__":
    test_min_eating_speed()