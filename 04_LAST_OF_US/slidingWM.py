from typing import List
from collections import deque
from sortedcontainers import SortedDict

class Solution:

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque([])
        cur_max = max(nums[:k])
        result = [cur_max]
        sd = SortedDict()

        for i, num in enumerate(nums):

            print(f"i: {i}, num: {num}, queue: {queue}, sd: {sd}, result: {result}")

            if i < k:
                queue.append([i, num])
                if num not in sd:
                    sd[num] = set()
                sd[num].add(i)
            else:
                queue.append([i, num])
                j, val = queue.popleft()
                print(f"Popped from queue - j: {j}, val: {val}")
                if len(sd[val]) == 1:
                    del sd[val]
                else:
                    sd[val].remove(j)

                if num not in sd:
                    sd[num] = set()
                sd[num].add(i)

                if num > cur_max:
                    cur_max = num
                else:
                    cur_max = sd.peekitem(-1)[0]

                result.append(cur_max)

        return result

