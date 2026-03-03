class Node:
    def __init__(self, value):
        self.connections = []
        self.value = value
    
    def add_connection(self, value):
        new_node = Node(value)
        self.connections.append(new_node)
        return new_node

def dfs(node):
    if node == None:
        return
    for i in range(len(node.connections)):
        dfs(node.connections[i])
    print(node.value)

"""
1-3-5-7
|       
2-4-6
|
3-6-9
"""
def construct_graph():
    parent_node = Node(1)
    three = parent_node.add_connection(3)
    five = three.add_connection(5)
    five.add_connection(7)

    two = parent_node.add_connection(2)
    four = two.add_connection(4)
    three_2 = two.add_connection(3)
    return parent_node

def main():
    parent = construct_graph()
    dfs(parent)

if __name__ == '__main__':
    main()