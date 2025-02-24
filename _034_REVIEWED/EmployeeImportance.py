"""
# Definition for Employee.
"""
# https://leetcode.com/problems/employee-importance/
class Employee(object):
    def __init__(self, id, importance, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution(object):
    def getImportance(self, employees : list[Employee], id : int) -> int:
        emp_id_to_imp_subs_mapping = {}
        for emp in employees:
            emp_id_to_imp_subs_mapping[emp.id] = (emp.importance, emp.subordinates)

        return self.getImportanceHelper(emp_id_to_imp_subs_mapping, id)
        
    def getImportanceHelper(self, emp_id_to_imp_subs_mapping, id) -> int:
        importance = emp_id_to_imp_subs_mapping[id][0]

        for sub_id in emp_id_to_imp_subs_mapping[id][1]:
            importance += self.getImportanceHelper(emp_id_to_imp_subs_mapping, sub_id)
            
        return importance
