from typing import List
import bisect

class Solution5:
    def numTeams(self, rating: List[int]) -> int:
        sorted_list = []
        smaller = [0 for _ in range(len(rating))]
        bigger = [0 for _ in range(len(rating))]
        for i in range(len(rating)):
            # print("i:" + str(rating[i]))
            if len(sorted_list) > 0:
                # check for smaller and bigger
                smaller[i] += bisect.bisect_left(sorted_list, rating[i])
                bigger[i] += len(sorted_list) - bisect.bisect_right(sorted_list, rating[i])

            # print(smaller)
            # print(bigger)
            # print(rating)
            bisect.insort(sorted_list, rating[i])
            # print(sorted_list)

        total = 0
        for j in range(1, len(rating) - 1):
            val_j = rating[j]
            for k in range(j + 1, len(rating)):
                val_k = rating[k]
                if val_k > val_j:
                    total += smaller[j]
                elif val_k < val_j:
                    total += bigger[j]
        return total 