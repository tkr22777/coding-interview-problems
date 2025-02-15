from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        sorted_by_diff_profit = sorted(list(zip(difficulty, profit)), key=lambda x: x[0])
        # print(sorted_by_diff_profit)

        sorted_by_diff_max_profit = []
        max_profit = 0
        for v in sorted_by_diff_profit:
            if v[1] > max_profit:
                max_profit = v[1]
            sorted_by_diff_max_profit.append([v[0], max_profit])

        # print(sorted_by_diff_max_profit)
        def bin_search_max_profit_max_index(array, max_diff):
            left = 0
            right = len(sorted_by_diff_max_profit) - 1
            while left <= right:
                mid = (left + right) // 2
                if array[mid][0] <= max_diff:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        total = 0
        for w in worker:
            i = bin_search_max_profit_max_index(sorted_by_diff_max_profit, w)
            # print(" i:" + str(i - 1) + " max for w:" + str(w))
            # when left is zero from bin search, it never moved forward as the value is bigger than w
            if i - 1 >= 0:
                max_profit_for_w = sorted_by_diff_max_profit[i - 1][1]
                # print(" i:" + str(i - 1) + " max for w:" + str(w) + "," + str(max_profit_for_w))
                total += max_profit_for_w
        return total


s = Solution()
print("1st case:" + str(100 == s.maxProfitAssignment([2, 4, 6, 8, 10], [10, 20, 30, 40, 50], [4, 5, 6, 7])))
print("2nd case:" + str(190 == s.maxProfitAssignment([13, 37, 58], [4, 90, 96], [34, 73, 45])))