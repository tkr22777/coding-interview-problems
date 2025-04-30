"""
Coin Change Problem

Problem Summary:
Given an array of coin denominations (coins) and a target amount, 
find the minimum number of coins needed to make up the amount.
If the amount cannot be made up by any combination of the coins, return -1.

Example:
- Input: coins = [1, 2, 5], amount = 11
- Output: 3 (5 + 5 + 1 = 11, using 3 coins)

Algorithm:
This implementation uses a top-down dynamic programming approach (memoization)
to efficiently calculate the minimum number of coins needed for each amount
from 1 to the target amount, avoiding redundant calculations.

Time Complexity: O(amount * number of coins)
Space Complexity: O(amount) for the memoization cache
"""

from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Cache to store already computed results
        memo = {}
        
        def min_coins_needed(remaining_amount: int) -> int:
            """
            Returns the minimum number of coins needed to make up the remaining amount.
            Returns -1 if it's impossible to make up the amount with given coins.
            """
            # Base cases
            if remaining_amount == 0:  # Successfully used coins to reach target
                return 0
            if remaining_amount < 0:   # Over-shot the target amount
                return -1
            if remaining_amount in memo:  # Return cached result if available
                return memo[remaining_amount]
            
            # Try each coin and find the minimum number of coins needed
            best_result = float('inf')  # Initialize with infinity instead of amount + 1
            
            for coin in coins:
                # Recursively try using this coin
                result = min_coins_needed(remaining_amount - coin)
                
                # If we found a valid combination using this coin
                if result >= 0:
                    best_result = min(best_result, result + 1)
            
            # Cache and return the final result
            memo[remaining_amount] = -1 if best_result == float('inf') else best_result
            return memo[remaining_amount]
        
        return min_coins_needed(amount)

# Test cases
s = Solution()
print(s.coinChange([1, 2, 5], amount = 11) == 3)
print(s.coinChange([1, 2, 5], amount = 13) == 4)
print(s.coinChange([1], amount = 0) == 0)
print(s.coinChange([2], amount = 3) == -1)
print(s.coinChange([187,419,83,408], 6249) == 19)