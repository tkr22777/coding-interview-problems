#!/usr/bin/python
"""
Question:

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None

    def append(self, anotherList):
        self.next = anotherList

    def appendNumber(self, number):
        if self.next == None:
            self.append(ListNode(number))
        else:
            self.next.appendNumber(number)

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + " -> " + str(self.next)

class Solution(object):

    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    def addTwoNumbers(self, l1, l2):

        if l1 is None and l2 is None:
            return None

        return self.addTwoNumbersHelper(l1, l2, 0);

    def addTwoNumbersHelper(self, l1, l2, carry):

        if l1 is None and l2 is None:
            if carry is 1:
                return ListNode(1)
            else:
                return None

        currentSum = carry

        if l1 is not None:
            currentSum = currentSum + l1.val

        if l2 is not None:
            currentSum = currentSum + l2.val

        currentCarry = 0

        if currentSum > 9:
            currentCarry = 1 
            currentSum = currentSum % 10

        l1Next = None
        if l1 is not None:
            l1Next = l1.next

        l2Next = None
        if l2 is not None:
            l2Next = l2.next

        lsum = ListNode(currentSum)
        lsum.next = self.addTwoNumbersHelper(l1Next, l2Next, currentCarry);

        return lsum


#Number 243
list1 = ListNode(2)
list1.appendNumber(4)
list1.appendNumber(3)
print list1

#Number 243
list2 = ListNode(5)
list2.appendNumber(6)
list2.appendNumber(4)
print list2

summer = Solution()
print summer.addTwoNumbers(list1 , list2)

