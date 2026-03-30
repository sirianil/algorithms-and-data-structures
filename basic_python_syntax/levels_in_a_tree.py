from tree import Node

class LevelsInATree:
    def return_tree_levels(self, node):
        levels = []
        def dfs(node, height):
            if not node:
                return
            
            if height == len(levels):          # First time visiting this depth
                levels.append([])
            levels[height].append(node.value)

            dfs(node.rightNode, height+1)
            dfs(node.leftNode, height+1)

        dfs(node, 0)
        return levels

def construct_tree():
    parent = Node(5)
    parent.assign_left_node(Node(0))
    parent.assign_right_node(Node(10))
    return parent

if __name__ == '__main__':
    parent = construct_tree()
    l = LevelsInATree()
    print(l.return_tree_levels(parent))
    