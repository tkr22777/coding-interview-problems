"""
Maximum Profit Assignment
Assign jobs to workers to maximize total profit.

Given:
- difficulty[i]: Difficulty level of ith job
- profit[i]: Profit of ith job
- worker[j]: Ability level of jth worker

A worker can only be assigned to a job if their ability >= job difficulty.
Each worker can be assigned at most one job, but jobs can remain unassigned.
Return the maximum profit we can achieve.

Example: 
- difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
- Maximum profit = 100 (worker with ability 4→job with difficulty 4 (profit 20), etc.)

Time Complexity: O(n log n + m log n) where n = jobs, m = workers
Space Complexity: O(n) for the sorted job arrays
"""

from typing import List

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        """
        Calculate maximum total profit by optimally assigning jobs to workers.
        
        Args:
            difficulty: List of job difficulty levels
            profit: List of corresponding job profits
            worker: List of worker ability levels
            
        Returns:
            Maximum possible total profit
        """
        # Sort jobs by difficulty
        jobs_by_difficulty = sorted(list(zip(difficulty, profit)), key=lambda x: x[0])
        
        # Track maximum profit at each difficulty level
        difficulty_max_profit_pairs = []
        max_profit_so_far = 0
        
        for diff, prof in jobs_by_difficulty:
            if prof > max_profit_so_far:
                max_profit_so_far = prof
            difficulty_max_profit_pairs.append([diff, max_profit_so_far])
        
        def find_max_profit_index(jobs_array, max_difficulty):
            """
            Find the insertion point (one past the rightmost index) where job difficulty <= worker ability.
            
            This binary search implementation uses 'right = mid - 1' when the condition is false because:
            1. We're looking for the rightmost index where difficulty <= worker ability
            2. When jobs_array[mid][0] > max_difficulty, mid is definitely not valid, so we move left (right = mid - 1)
            3. When jobs_array[mid][0] <= max_difficulty, mid might not be the rightmost valid index, so we move right
            4. After the loop, 'left' points to the insertion point (one past the rightmost valid index)
            5. Therefore, to access the last valid job, we use jobs_array[idx-1]
            
            If we used 'right = mid' instead, we'd risk an infinite loop when the condition is false.
            
            Args:
                jobs_array: Sorted array of [difficulty, max_profit] pairs
                max_difficulty: Maximum difficulty a worker can handle
                
            Returns:
                Insertion point (one past the rightmost valid index)
            """
            left = 0
            right = len(jobs_array) - 1
            
            while left <= right:
                mid = (left + right) // 2
                if jobs_array[mid][0] <= max_difficulty:
                    # This job is doable, but might not be the rightmost valid job.
                    # Continue searching to the right.
                    left = mid + 1
                else:
                    # This job is too difficult. Must search to the left.
                    # Using 'right = mid - 1' to avoid infinite loops.
                    right = mid - 1
                    
            return left  # Return insertion point (one past the rightmost valid index)
        
        # Calculate total profit
        total_profit = 0
        for worker_ability in worker:
            # Find maximum index where difficulty <= worker_ability
            idx = find_max_profit_index(difficulty_max_profit_pairs, worker_ability)
            
            # Only add profit if worker can do at least one job
            # We use idx-1 because idx points to the insertion point (one past the rightmost valid job)
            if idx - 1 >= 0:
                worker_profit = difficulty_max_profit_pairs[idx - 1][1]
                total_profit += worker_profit
                
        return total_profit


def test_max_profit_assignment():
    """Test the maxProfitAssignment function with various test cases."""
    solution = Solution()
    
    # Test case 1: Basic case from problem description
    test_cases = [
        # (difficulty, profit, worker, expected_result, description)
        (
            [2, 4, 6, 8, 10], 
            [10, 20, 30, 40, 50], 
            [4, 5, 6, 7], 
            100,
            "Basic test case"
        ),
        (
            [13, 37, 58], 
            [4, 90, 96], 
            [34, 73, 45], 
            190,
            "Workers with higher abilities"
        ),
        (
            [], [], [], 0,
            "Empty inputs"
        )
    ]
    
    for i, (diff, prof, workers, expected, description) in enumerate(test_cases, 1):
        result = solution.maxProfitAssignment(diff, prof, workers)
        assert result == expected, f"Test case {i} failed: {description}"
    
    print("All maximum profit assignment tests passed!")


if __name__ == "__main__":
    test_max_profit_assignment()