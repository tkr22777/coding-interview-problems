#!/usr/bin/python
"""
Question:

You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
class ListNode:

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + " -> " + str(self.next)

class Solution:

    def addTwoNumbers(self, l1, l2):

        return self.addTwoNumbersHelper(l1, l2, 0)

    def addTwoNumbersHelper(self, l1, l2, carry):

        if l1 is None and l2 is None:
            if carry == 1:
                return ListNode(1)
            else:
                return None

        currentSum = carry

        if l1 is not None:
            currentSum = currentSum + l1.val

        if l2 is not None:
            currentSum = currentSum + l2.val

        carry = 0

        if currentSum > 9:
            carry = 1 
            currentSum = currentSum % 10

        l1Next = None
        if l1 is not None:
            l1Next = l1.next

        l2Next = None
        if l2 is not None:
            l2Next = l2.next

        summedNode = ListNode(currentSum)
        summedNode.next = self.addTwoNumbersHelper(l1Next, l2Next, carry)

        return summedNode

    def addTwoNumbersIterative(self, l1, l2):
        """
        Adds two numbers represented by linked lists using an iterative approach.
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        currentNode = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0

            currentSum = val1 + val2 + carry
            carry = currentSum // 10
            digit = currentSum % 10

            newNode = ListNode(digit)
            currentNode.next = newNode
            currentNode = currentNode.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        return dummyHead.next

#Number 243
list1 = ListNode(2)
list1Nxt = ListNode(4)
list1.next = list1Nxt
list1Nxt.next = ListNode(3)
print(list1)

#Number 564
list2 = ListNode(5)
list2Nxt = ListNode(6)
list2.next = list2Nxt
list2Nxt.next = ListNode(4)
print(list2)

summer = Solution()
print(summer.addTwoNumbers(list1 , list2))
