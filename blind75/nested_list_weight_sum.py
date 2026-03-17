# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger:
   def __init__(self, value=None):
       """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def add(self, elem):
       """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

   def setInteger(self, value):
       """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       The result is undefined if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       The result is undefined if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """

class Solution:
    '''
    iterate over values:
        call method to calculate weight => pass nestedInteger and depth=1

    helper method: nestedInteger, depth
        if nestedInteger.isInteger():
            return getInteger() * depth
        
        nested_list = nestedInteger.getList():
        if nested_list:
            total_weight = 0
            for i in range(nested_list):
                total_weight += helper => item - increment the depth
    '''
    def depthSum(self, nestedList) -> int:
        self.calculateWeight(nestedList, 1)

    def calculateWeight(self, nestedList, depth):
        if nestedList.isInteger():
            return nestedList.getInteger() * depth
        
        nested_list = nestedList.getList()
        if nested_list:
            total_weight = 0
            for i in range(len(nested_list)):
                total_weight += self.calculateWeight(nested_list[i], depth+1)
            return total_weight
