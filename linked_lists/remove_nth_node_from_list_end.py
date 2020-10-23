# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @return the head node in the linked list
    def removeNthFromEnd(self, A, B):
        nA = 0
        kA = A
        
        while kA:
            nA += 1
            kA = kA.next
            
        if B >= nA:
            return A.next
            
        iA = nA - B
        
        kA = A
        prev = None
        while kA and iA > 0:
            prev = kA
            kA = kA.next
            iA -= 1
            pass
        
        prev.next = kA.next
        return A
        
