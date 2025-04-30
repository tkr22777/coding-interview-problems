# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """

        i = 0
        nums = []
        answer = []
        candidates = set()

        cursor = head
        while cursor is not None:
            nums.append(cursor.val)
            answer.append(0)
            cursor = cursor.next
            i = i + 1

        completed = set()
        for i in range(len(nums)):
            toRemove = set()
            for j in candidates:
                if nums[i] > nums[j] and answer[j] is 0:
                        answer[j] = nums[i]
                        toRemove.add(j)

            candidates.add(i)
            candidates = candidates - toRemove

        return answer


