class DLLNode:
    def __init__(self, val):
        self.val = val
        self.next = self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def addToTail(self, val):
        node = DLLNode(val)
        
        if self.tail == None:
            self.tail = self.head = node
        else:
            self.tail.next = node
            self.tail = node
        self.length = self.length + 1
        return node
    
    def removeNode(self, node):
        if node == None:
            return
        if node.prev != None:
            node.prev.next = node.next
        if node.next != None:
            node.next.prev = node.prev

    def traverse(self):
        current = self.head
        while current != None:
            print(current.val)
            current = current.next

def main():
    dll = DoublyLinkedList()
    dll.addToTail(1)
    dll.addToTail(2)
    threeNode = dll.addToTail(3)
    dll.addToTail(4)
    dll.addToTail(5)
    dll.removeNode(threeNode)
    dll.traverse()

if __name__ == '__main__':
    main()

            

