class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def maximum_depth(root):
    return dfs(root)

def dfs(root):
    if root == None:
        return 0
    left_depth = dfs(root.left)
    right_depth = dfs(root.right)

    return max(left_depth, right_depth) + 1