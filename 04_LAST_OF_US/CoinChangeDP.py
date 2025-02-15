from typing import List

class Solution:
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