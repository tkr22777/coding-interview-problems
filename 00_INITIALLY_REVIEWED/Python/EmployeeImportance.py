"""
# Problem Summary:
# You are given a data structure representing a company's employee hierarchy and importance values.
# Each employee has a unique ID, an importance value, and a list of direct subordinates' IDs.
# The goal is to calculate the total importance value of an employee and all their subordinates.
# 
# Example:
# Input: employees = [[1,5,[2,3]],[2,3,[]],[3,3,[]]], id = 1
# Output: 11
# Explanation: Employee 1 has importance value 5 and has two direct subordinates: 2 and 3.
# Employee 2 has importance value 3 and no subordinates.
# Employee 3 has importance value 3 and no subordinates.
# So the total importance value of employee 1 is 5 + 3 + 3 = 11.
"""
# https://leetcode.com/problems/employee-importance/
from collections import deque

class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees : list[Employee], id : int) -> int:
        # Map each employee ID to (importance, subordinates)
        emp_id_to_imp_subs_mapping = {}
        for emp in employees:
            emp_id_to_imp_subs_mapping[emp.id] = (emp.importance, emp.subordinates)
            
        # DFS approach
        return self.getImportanceHelper(emp_id_to_imp_subs_mapping, id)
    
    def getImportanceHelper(self, emp_id_to_imp_subs_mapping, id) -> int:
        if id not in emp_id_to_imp_subs_mapping:
            return 0
            
        importance = emp_id_to_imp_subs_mapping[id][0]
        
        for sub_id in emp_id_to_imp_subs_mapping[id][1]:
            importance += self.getImportanceHelper(emp_id_to_imp_subs_mapping, sub_id)
            
        return importance
        
    # Iterative BFS solution
    def getImportanceIterative(self, employees : list[Employee], id : int) -> int:
        emp_map = {emp.id: emp for emp in employees}
        
        if id not in emp_map:
            return 0
            
        total = 0
        queue = deque([id])
        
        while queue:
            curr_id = queue.popleft()  # O(1) operation with deque
            curr_emp = emp_map[curr_id]
            
            total += curr_emp.importance
            queue.extend(curr_emp.subordinates)
            
        return total
