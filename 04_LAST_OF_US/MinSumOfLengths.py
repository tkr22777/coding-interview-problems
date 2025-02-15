from typing import List

class Solution:
    def minSumOfLengths_2(self, arr: List[int], target: int) -> int:
        ag_sum = []
        s = 0
        for v in arr:
            s += v
            ag_sum.append(s)
        print(ag_sum)

        def sub_sum(ag_sum, i, j):
            return -1

        return -1

    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        # print("array: " + str(arr))
        def sub_array_sum(sum_cache: dict, arr: List[int], i: int, j: int) -> int:
            if i == j:
                return 0

            key = i * 10000 + j
            if key in sum_cache:
                return sum_cache[key]

            sum_cache[key] = sub_array_sum(sum_cache, arr, i, j - 1) + arr[i]
            return sum_cache[key]

        sum_cache = {}
        min_len = -1
        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                sum_ij = sub_array_sum(sum_cache, arr, i, j)
                if sum_ij > target:
                    break
                if sum_ij == target:
                    for k in range(j, len(arr)):
                        for l in range(k + 1, len(arr) + 1):
                            sum_kl = sub_array_sum(sum_cache, arr, k, l)
                            if sum_kl > target:
                                break
                            if sum_kl == target:
                                if min_len == -1:
                                    min_len = (j - i) + (l - k)
                                else:
                                    min_len = min((j - i) + (l - k), min_len)

        # print("min len:" + str(min_len))
        return min_len


s = Solution()
# print("1st case:" + str(2 == s.minSumOfLengths([3,2,2,4,3], 3)))
# print("2nd case:" + str(2 == s.minSumOfLengths([7,3,4,7], 7)))
# print("3rd case:" + str(-1 == s.minSumOfLengths([4, 3, 2, 6, 2, 3, 4], 6)))
print("3rd case:" + str(-1 == s.minSumOfLengths_2([4, 3, 2, 6, 2, 3, 4], 6))) 