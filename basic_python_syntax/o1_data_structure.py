from collections import defaultdict

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Solution:
    def __init__(self):
        self.hash_map = defaultdict(list)
        self.head = None
        self.tail = None

    def insert(self, val):
        node = Node(val)



if __name__ == '__main__':
    s = Solution()
    s.insert()
    s.remove()
    s.getRandom()