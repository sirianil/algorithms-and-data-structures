class Node:
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None

def balanced_binary_tree(root):
    (left_height, right_height) = dfs(root)
    if int(left_height - right_height) > 1:
        return False
    else:
         return True

def dfs(root):
    if root == None:
        return 0
    
    left_height = dfs(root.left)
    right_height = dfs(root.right)

    return (left_height+1, right_height+1)

def main():
    print("Starting main function")

if __name__ == '__main__':
    main()