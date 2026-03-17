# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

'''
any node that has no left and right child is a leaf;
dfs -> when you find a leaf, add it to the list.
and return the list along with if it is a leaf and then recruse.
'''

class Solution:
    def findLeaves(self, root):
        final_list = []
        while root.left or root.right:
            final_list.append(self.dfs(root))
    
    def dfs(self, node):
        if node == None:
            []

        if node.left == None and node.right == None: # it is a leaf
            return [node.val]
        
        leaves = []
        leaves.extend(self.dfs(node.right))
        leaves.extend(self.dfs(node.left))

        return leaves
    