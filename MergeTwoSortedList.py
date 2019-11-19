#!/usr/bin/python

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

     def __str__(self):
         node = self;
         return_str = "Head"
         while node.next is not None:
             return_str = return_str + " -> " +  str(node.val)
             node = node.next
         return return_str

     def append(self, y):
         node = self;
         while node.next is not None:
             node = node.next
         node.next = ListNode(y)

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNod
        """

        if l1 is None and l2 is None:
            return None

        if l1 is None:
            return l2;

        if l2 is None:
            return l1;

        mergedList = None
        mergedListPointer = None

        l1Pointer = l1;
        l2Pointer = l2;

        while l1Pointer is not None or l2Pointer is not None:

            if mergedListPointer is None:
                mergedListPointer = ListNode(-1)
                mergedList = mergedListPointer
            else:
                mergedListPointer.next = ListNode(-1)
                mergedListPointer = mergedListPointer.next

            if l1Pointer is None:
                mergedListPointer.val = l2Pointer.val
                l2Pointer = l2Pointer.next

            elif l2Pointer is None:
                mergedListPointer.val = l1Pointer.val
                l1Pointer = l1Pointer.next

            elif l1Pointer.val < l2Pointer.val:
                mergedListPointer.val = l1Pointer.val
                l1Pointer = l1Pointer.next
            else:
                mergedListPointer.val = l2Pointer.val;
                l2Pointer = l2Pointer.next

        return mergedList

list1 = ListNode(1)
list1.append(3)
list1.append(5)
list1.append(9)

print list1

list2 = ListNode(2)
list2.append(6)
list2.append(8)
list2.append(10)

print list2

sol = Solution()
mergedList = sol.mergeTwoLists(list1, list2)

print mergedList
