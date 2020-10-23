# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def reorderList(self, A):
        nA = 0
        K = A
        
        As = []
        
        while K:
            As.append(K)
            K = K.next
            nA += 1
            
        i = 0
        n = nA-1
        prev = None
        while n > i:
            As[i].next = As[n]
            if prev:
                prev.next = As[i]
            prev = As[n]
            i += 1
            n -= 1
            
        if n == i and prev:
            prev.next = As[i]
            prev = As[i]
        
        if prev:   
            prev.next = None
            
        return As[0]
            
        
