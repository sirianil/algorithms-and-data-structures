class Node:
    def __init__(self, value):
        self.value = value
        self.leftNode = None
        self.rightNode = None
    
    def print_left_node(self):
        if (self.leftNode == None):
            print("Left node is not assigned")
        else:
            print(self.leftNode.value)

    def print_right_node(self):
        if (self.rightNode == None):
            print("Right node is not assigned")
        else:
            print(self.rightNode.value)
    
    def assign_left_node(self, node):
        self.leftNode = node

    def assign_right_node(self, node):
        self.rightNode = node

def dfs(node):
    if node == None:
        return
    dfs(node.leftNode)
    print(node.value)
    dfs(node.rightNode)

def construct_tree():
    parent = Node(5)
    parent.assign_left_node(Node(0))
    parent.assign_right_node(Node(10))
    return parent

def bfs(node):
    node_queue = [node]
    while len(node_queue) != 0:
        node = node_queue.pop()
        print(node.value)
        if node.leftNode != None:
            node_queue.append(node.leftNode)
        if node.rightNode != None:
            node_queue.append(node.rightNode)

if __name__ == '__main__':
    parent = construct_tree()
    dfs(parent)
    bfs(parent)