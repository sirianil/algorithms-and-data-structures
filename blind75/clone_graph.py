class Solution:
    def __init__(self):
        self.mapping = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        
        if node in self.mapping:
            return self.mapping[node]
            
        # Create clone and store in map before recursing
        clone = Node(node.val)
        self.mapping[node] = clone
        
        # Build neighbor list recursively
        for neighbor in node.neighbors:
            clone.neighbors.append(self.cloneGraph(neighbor))
            
        return clone