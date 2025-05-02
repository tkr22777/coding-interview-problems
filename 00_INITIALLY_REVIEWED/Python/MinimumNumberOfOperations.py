from typing import List
from collections import deque

class Solution:
    """
    Problem: Find minimum operations to transform 'start' into 'goal'.
    For each step, we can: add, subtract, or XOR any number from 'nums'.
    Valid values must be between 0 and 1000 inclusive.
    Returns -1 if goal can't be reached.
    """
    def minimumOperations(self, nums: List[int], start: int, goal: int) -> int:
        if start == goal:
            return 0
            
        visited = set()
        queue = deque([(start, 0)])  # (value, operations)
        
        while queue:
            current, steps = queue.popleft()
            
            if current == goal:
                return steps
                
            if current in visited or not (0 <= current <= 1000):
                continue
                
            visited.add(current)
            
            for num in nums:
                queue.append((current + num, steps + 1))
                queue.append((current - num, steps + 1))
                queue.append((current ^ num, steps + 1))
                
        return -1
        
    def minimumOperationsOriginal(self, nums: List[int], start: int, goal: int) -> int:
        """
        Original implementation using a different BFS approach.
        """
        if start == goal:
            return 0

        visited = set()
        queue = deque([start])
        depth = 1
        while queue:
            breadth = len(queue)
            for _ in range(breadth):
                current = queue.popleft()
                if current in visited:
                    continue
                
                if current == goal:
                    return depth - 1
                elif 0 <= current and current <= 1000:
                    visited.add(current)
                    for num in nums:
                        queue.append(current + num)
                        queue.append(current - num)
                        queue.append(current ^ num)
                # print("depth: " + str(depth) + ", breadth:" + str(breadth) + ", current: " + str(current))
            depth += 1
        return -1

# Test cases
s = Solution()
print("Testing improved solution:")
print(s.minimumOperations(nums = [2,4,12], start = 2, goal = 12) == 2)
print(s.minimumOperations(nums = [3,5,7], start = 0, goal = -4) == 2)
print(s.minimumOperations(nums = [2,8,16], start = 0, goal = 1) == -1)

print("\nTesting original solution:")
print(s.minimumOperationsOriginal(nums = [2,4,12], start = 2, goal = 12) == 2)
print(s.minimumOperationsOriginal(nums = [3,5,7], start = 0, goal = -4) == 2)
print(s.minimumOperationsOriginal(nums = [2,8,16], start = 0, goal = 1) == -1)

