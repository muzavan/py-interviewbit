# Definition for singly-linked list with a random pointer.
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution:
    # @param head, a RandomListNode
    # @return a RandomListNode
    def copyRandomList(self, head):
        orhead = head
        prevHead = RandomListNode(0)
        prev = prevHead
        d = {}
        while orhead:
            curr = RandomListNode(orhead.label)
            d[orhead] = curr
            prev.next = curr
            prev = curr
            
            orhead = orhead.next
            
        curr = prevHead.next
        orhead = head
        
        while orhead:
            curr.random = d[orhead.random] if orhead.random else None
            curr = curr.next
            orhead = orhead.next
        
        
        return prevHead.next
            
        
