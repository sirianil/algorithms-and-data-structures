
"""
Time of Start: 
Time at start solutioning:
Time at start coding:
time at testing:
time at submission:
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def linked_list_cycle(self, head):
        slow = fast = head

        while fast and fast.next:
            if slow == fast:
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        return False


if __name__ == '__main__':
    s = Solution()