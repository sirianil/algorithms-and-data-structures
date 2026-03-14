# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int):
        if head == None:
            return

        fast = head
        current_count = 0
        while fast and current_count != n:
            fast = fast.next
            current_count += 1

        slow = head
        slow_prev = None
        while fast:
            slow_prev = slow
            slow = slow.next
            fast = fast.next

        if slow_prev == None:
            slow = slow.next
            return slow
        else:
            slow_prev.next = slow.next
            return head

    def traverse_and_print_list(self,head):
        cur = head
        while cur:
            print(cur.val)
            cur = cur.next        

if __name__ == '__main__':
    s = Solution()
    lll = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9, ListNode(10))))))))))
    s.traverse_and_print_list(lll)
    lll = ListNode(1, ListNode(2))
    res = s.removeNthFromEnd(lll, 2)
    s.traverse_and_print_list(res)