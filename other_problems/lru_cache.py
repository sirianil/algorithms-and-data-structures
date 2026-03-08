class DLLNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = self.prev = None

class LRUCache:
    '''
    Initialize the LRU Cach
    '''
    def __init__(self, capacity):
        self.cache = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
    
    def get(self, key):
        if key not in self.cache:
            return None
        
        node = self.cache[key]
        self.moveNodeToHead()

    def moveNodeToHead(self, node):
        self.head.next = node
        node.prev = self.head

        node.prev.next = node.next
        node.next.prev = node.prev
    
    def put(self, key, value):
        if len(self.cache) == self.capacity:
            return
    
    def removeNodeFromDLL(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    


    

