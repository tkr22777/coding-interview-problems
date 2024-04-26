"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        emp_id_to_imp_subs_mapping = {}
        for emp in employees:
            emp_id_to_imp_subs_mapping[emp.id] = (emp.importance, emp.subordinates)
        # print(emp_id_to_imp_subs_mapping)

        return self.getImportanceHelper(emp_id_to_imp_subs_mapping, id)
        
    def getImportanceHelper(self, emp_id_to_imp_subs_mapping, id):
        importance = emp_id_to_imp_subs_mapping[id][0]

        for sub_id in emp_id_to_imp_subs_mapping[id][1]:
            importance += self.getImportanceHelper(emp_id_to_imp_subs_mapping, sub_id)
            
        return importance
