# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    stack = []
    next_val = None

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack.append(nestedList)

    def next(self):
        """
        :rtype: int
        """
        return self.next_val

                
    def hasNext(self):
        """
        :rtype: bool
        """
        found = False
        while not found and len(self.stack) > 0:
            nested_list = self.stack.pop()
            if isinstance(nested_list, list):
                nested_list.reverse()
                for nested_int in nested_list:
                    self.stack.append(nested_int)
            elif nested_list.isInteger():
                found = True
                self.next_val = nested_list.getInteger()
            else:
                nested_list = nested_list.getList()
                nested_list.reverse()
                for nested_int in nested_list:
                    self.stack.append(nested_int)
        return found

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
