from collections import defaultdict
from sortedcontainers import SortedDict
from typing import List

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        num_map = defaultdict(int)
        for num in arr:
            num_map[num] += 1
        # print("num_map: " + str(num_map))

        count_to_nums_map = SortedDict()
        for num, count in num_map.items():
            if count not in count_to_nums_map:
                count_to_nums_map[count] = set()
            count_to_nums_map[count].add(num)

        # print("count_to_nums_map:" + str(count_to_nums_map))

        done = False
        result = 0
        for count, nums in count_to_nums_map.items():
            # print("before count: " + str(count) + " nums:" + str(nums) + " k: " + str(k) + " result:" + str(result))
            if done:
                result += len(nums)
            else:
                for i in range(len(nums)):
                    if k >= count:
                        k -= count
                    else:
                        done = True
                        result += len(nums) - i
                        break
            # print("after count: " + str(count) + " nums:" + str(nums) + " k: " + str(k) + " result:" + str(result))
        return result
