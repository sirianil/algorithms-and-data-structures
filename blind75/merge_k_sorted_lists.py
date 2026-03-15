# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class Solution:
    def mergeKLists(self, lists):
        min_heap = []
        merged_head = prev = None
        counter = 0

        for i in range(len(lists)):
            node = lists[i]
            if node != None:
                heapq.heappush(min_heap, (node.val,  counter, node))
                counter += 1

        while min_heap:
            val, _, node = heapq.heappop(min_heap)
            if node.next:
                heapq.heappush(min_heap, (node.next.val, counter, node.next))
                counter += 1
            
            if merged_head == None:
                merged_head = node
                prev = node
            else:
                prev.next = node
                prev = node

        return merged_head

        