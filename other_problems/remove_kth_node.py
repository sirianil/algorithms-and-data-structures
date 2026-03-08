class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def remove_kth_node(parent, k):
    fast = parent

    counter = 0
    while (fast != None and counter < k):
        fast = fast.next

    slow = parent
    while fast != None:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next

    return parent

def traverse_linked_list(root):
    current = root

    while current != None:
        print(current.val, " -> ")
        current = current.next

if __name__ == '__main__':
    root1 = ListNode(3, ListNode(6, ListNode(9, ListNode(12))))
    # root2 = ListNode(2, ListNode(4, ListNode(6, ListNode(8))))
    print("LL1 is ")
    traverse_linked_list(root1)
#    print("LL2 is ")
    # traverse_linked_list(root2)
    # print("merged LL is ")
    merged_root = remove_kth_node(root1, 2)
    traverse_linked_list(merged_root)    


    