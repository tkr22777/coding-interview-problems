from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recurse(coins: List[int], amount: int):
            if amount == 0:
                return 0
            
            if amount < 0:
                return -1
            
            if amount in memo:
                return memo[amount]
            
            min_coins = amount + 1
            for coin in coins:
                coin_count = recurse(coins, amount - coin)
                if coin_count >= 0:
                    min_coins = min(min_coins, coin_count + 1)
            
            if min_coins == amount + 1:
                memo[amount] = -1
                return -1
            else:
                memo[amount] = min_coins
                return min_coins

        return recurse(coins, amount)

    # bottom up, more efficient
    def coinChange(self, coins: List[int], amount: int) -> int:
        best_coin_combo = [amount + 1] * (amount + 1)
        best_coin_combo[0] = 0

        for cent in range(amount + 1):
            for coin in coins:
                if coin <= cent:
                    best_coin_combo[cent] = min(best_coin_combo[cent - coin] + 1, best_coin_combo[cent])

        return best_coin_combo[amount] if best_coin_combo[amount] != amount + 1 else -1

# Test cases
s = Solution()
print(s.coinChange([1, 2, 5], amount = 11))
print(s.coinChange([1, 2, 5], amount = 11) == 3)
print(s.coinChange([1], amount = 0) == 0)
print(s.coinChange([2], amount = 3) == -1)
print(s.coinChange([187,419,83,408], 6249) == 19) 

# print(s.coinChange([1], amount = 10000))
# print(s.coinChange([1], amount = 10000) == 10000)

# 1, 2, 3
# 1 -> 1
# 2 -> 1
# 3 -> 1
# 4 -> 2
# 5 -> 2
# 6 -> 2
# 7 -> 2
# 8 -> 3

