class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    pointer1 = list1
    pointer2 = list2

    previous_node = None
    root_node = None

    while pointer1 != None and pointer2 != None:
        if pointer1.val > pointer2.val:
            if previous_node != None:
                previous_node.next = pointer2
            if root_node == None:
                root_node = pointer2
            previous_node = pointer2
            pointer2 = pointer2.next
        else:
            if previous_node != None:
                previous_node.next = pointer1
            if root_node == None:
                root_node = pointer1
            previous_node = pointer1
            pointer1 = pointer1.next
    
    while pointer1 != None:
        if previous_node != None:
            previous_node.next = pointer1
        if root_node == None:
            root_node = pointer1
        previous_node = pointer1
        pointer1 = pointer1.next

    while pointer2 != None:
        if previous_node != None:
            previous_node.next = pointer2
        if root_node == None:
            root_node = pointer2
        previous_node = pointer2
        pointer2 = pointer2.next

    return root_node

def traverse_linked_list(root):
    current = root

    while current != None:
        print(current.val, " -> ")
        current = current.next

if __name__ == '__main__':
    root1 = ListNode(3, ListNode(6, ListNode(9, ListNode(12))))
    root2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    print("LL1 is ")
    traverse_linked_list(root1)
    print("LL2 is ")
    traverse_linked_list(root2)
    print("merged LL is ")
    merged_root = mergeTwoLists(root1, root2)
    traverse_linked_list(merged_root)