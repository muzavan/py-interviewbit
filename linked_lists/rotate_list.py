# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def rotateRight(self, A, B):
        nA = 0
        K = A
        while K:
            nA += 1
            K = K.next
            
        if nA <= 1:
            return A
            
        start = nA - B
        start = start % nA
        
        prev = None
        
        K = A
        prev=None
        while K and start >= 0:
            if start == 0:
                if prev:
                    prev.next = None
                else:
                    return K
                break
            start -= 1
            prev = K
            K = K.next
            
        head = K
        while K.next:
            K = K.next
            
        K.next = A
        
        return head
        
            
        
            
            
        
        
