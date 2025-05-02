#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val):
         self.val = val
         self.next = None

     def __str__(self):
         node = self
         values = ["Head"]
         while node is not None:
             values.append(str(node.val))
             node = node.next
         return " -> ".join(values)

     def append(self, val):
         node = self
         while node.next is not None:
             node = node.next
         node.next = ListNode(val)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        Merge two sorted linked lists and return the head of the merged linked list.
        
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Create a dummy head node to simplify the merging process
        dummy_head = ListNode(-1)
        current = dummy_head
        
        # Iterate through both lists until one is exhausted
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # Attach the remaining nodes (if any)
        current.next = list1 if list1 else list2
        
        # Return the merged list (excluding the dummy head)
        return dummy_head.next

# Test code
list1 = ListNode(1)
list1.append(3)
list1.append(5)
list1.append(9)

print(list1)

list2 = ListNode(2)
list2.append(6)
list2.append(8)
list2.append(10)

print(list2)

solution = Solution()
merged_list = solution.mergeTwoLists(list1, list2)

print(merged_list)
