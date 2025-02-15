# https://leetcode.com/problems/minimum-number-of-operations-to-make-x-and-y-equal/
# is this BFS? do we need greedy, no need for queue?

from collections import deque

class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        b = 0
        q = deque()
        q.append(x)
        visited = set()
        while q:
            w = len(q)
            for _ in range(w):
                # print(q)
                v = q.popleft()
                # print("b:" + str(b) + " v:" + str(v))
                # sleep(0.1)

                if v in visited:
                    continue
                else:
                    visited.add(v)
                if v == y:
                    return b
                else:
                    if v < y:
                        q.append(v + 1)
                    else:  # v > y
                        if v % 11 == 0:
                            q.append(int(v / 11))
                        if v % 5 == 0:
                            q.append(int(v / 5))

                        q.append(v + 1)
                        q.append(v - 1)
            b += 1
        return b


s = Solution()
print(s.minimumOperationsToMakeEqual(26, 1) == 3)
print(s.minimumOperationsToMakeEqual(54, 2) == 4)
print(s.minimumOperationsToMakeEqual(1, 19) == 18)
print(s.minimumOperationsToMakeEqual(5, 2) == 2)
