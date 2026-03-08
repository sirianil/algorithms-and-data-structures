class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def traverse_linked_list(root):
    current = root

    while current != None:
        print(current.value, " -> ")
        current = current.next

# 1->2->3->4
# previous_node = None
# current_node = 1;
# 4->3->2->1

def reverse_linked_list(root):
    previous_node = None
    current_node = root
    next_node = None

    while (current_node != None):
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node
    return previous_node

if __name__ == '__main__':
    root = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
    traverse_linked_list(root)
    reversed_ll = reverse_linked_list(root)
    traverse_linked_list(reversed_ll)
