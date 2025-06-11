"""
Task Scheduler

Problem Statement:
You are given an array of CPU tasks, each represented by a letter, and a non-negative integer n that represents the cooldown period between two same tasks.
Each task takes one unit of time to execute. For each unit of time, the CPU could either complete one task or stay idle.
Return the least number of units of time that the CPU will take to finish all the given tasks.

Examples:
- Input: tasks = ["A","A","A","B","B","B"], n = 2
  Output: 8
  Explanation: 
  A -> B -> idle -> A -> B -> idle -> A -> B
  CPU executes tasks in this sequence: A, B, idle, A, B, idle, A, B, taking 8 units of time.

- Input: tasks = ["A","A","A","B","B","B"], n = 0
  Output: 6
  Explanation: No cooldown constraints, so CPU just executes all tasks in order, taking 6 units of time.

- Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
  Output: 16
  Explanation: The task A appears 6 times, so there must be at least 5 cooldowns between them.

Constraints:
- 1 <= tasks.length <= 10^4
- tasks[i] is an uppercase English letter
- 0 <= n <= 100
"""

from typing import List

def least_interval(tasks: List[str], cooldown_period: int) -> int:
    """
    Calculate the least number of units of time needed to execute all tasks with the given cooldown period.
    
    Args:
        tasks: A list of tasks represented by uppercase letters
        cooldown_period: The required idle time between two identical tasks
        
    Returns:
        The minimum time units required to complete all tasks
    
    Approach hints:
    - Count the frequency of each task
    - The task with the highest frequency is most constraining
    - Calculate the minimum slots needed based on the most frequent task
    - Consider optimizing by filling idle slots with less frequent tasks
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_least_interval():
    test_cases = [
        {"tasks": ["A","A","A","B","B","B"], "cooldown_period": 2, "expected": 8},
        {"tasks": ["A","A","A","B","B","B"], "cooldown_period": 0, "expected": 6},
        {"tasks": ["A","A","A","A","A","A","B","C","D","E","F","G"], "cooldown_period": 2, "expected": 16},
        {"tasks": ["A","A","A","B","B","B","C","C","C","D","D","E"], "cooldown_period": 2, "expected": 12},
        {"tasks": ["A","A","A","B","B","B"], "cooldown_period": 3, "expected": 10}
    ]
    
    for i, test_case in enumerate(test_cases):
        tasks = test_case["tasks"]
        cooldown_period = test_case["cooldown_period"]
        expected = test_case["expected"]
        result = least_interval(tasks, cooldown_period)
        status = "PASSED" if result == expected else f"FAILED (got {result}, expected {expected})"
        print(f"Test case {i+1}: {status}")


if __name__ == "__main__":
    # Uncomment the line below to run tests when you're ready
    # test_least_interval()
    
    # Example usage
    tasks = ["A","A","A","B","B","B"]
    cooldown_period = 2
    print(f"Least interval: {least_interval(tasks, cooldown_period)}") 