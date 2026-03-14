"""
Time of Start: 10:06
Time at start solutioning:
Time at start coding: 10:08
time at testing:
time at submission:
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    1 - 2 - 3- 4- 5- 6- 7- 8- 9- 10 
    First part:
        reamins the same - 1-2-3-4-5
    Second part:
        reverse it: 10-9-8-7-6
    merge:
        1-10-2-9-3-8- ... 
    how to reverse a ll?
    1-10-2-9-3-8-4-7-5-6
    """
    def reorder_list(self, head: ListNode):
        if head == None:
            return
        
        mid = self.find_center(head)
        reversed_mid = self.reverse_ll(mid)

        self.merge(head, reversed_mid)
        return head
    
    def merge(self, node1, node2):
        while node2.next:  # node2.next because reversed half ends at original head's neighbor
            next1 = node1.next
            next2 = node2.next
            node1.next = node2
            node2.next = next1
            node1 = next1
            node2 = next2
    
    def reverse_ll(self, head: ListNode):
        current = head # 2
        prev = None #1
        next = None 

        while current: # 1
            print("reversing LL")
            next = current.next #3
            current.next = prev # 
            prev = current #1
            current = next # 2

        return prev

    def find_center(self, head):
        slow = fast = head
        prev = None
        while fast and fast.next:
            print("Finding center")
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if prev:
            prev.next = None
        return slow
    
    def traverse_and_print_list(self,head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next

if __name__ == '__main__':
    s = Solution()
    lll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    s.traverse_and_print_list(lll)
    s.reorder_list(lll)
    s.traverse_and_print_list(lll)