# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop
class Solution:
    # @param A : list of linked list
    # @return the head node in the linked list
    def mergeKLists(self, A):
        h = []
        n = 0
        
        for node in A:
            while node:
                n += 1
                heappush(h, (node.val, node))
                node = node.next
                
        head = None
        curr = None
        for _ in range(n):
            tmp = heappop(h)
            if not head:
                head = tmp[1]
                curr = tmp[1]
            else:
                curr.next = tmp[1]
                curr = tmp[1]
        
        curr.next = None
        return head
                
