# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list
    def mergeTwoLists(self, A, B):
        kA = A
        kB = B
        
        head = None
        if kA.val <= kB.val:
            head = A
            kA = kA.next
        else:
            head = B
            kB = kB.next
            
            
        prev = head
            
            
        while kA and kB:
            a = kA.val
            b = kB.val
            
            if a <= b:
                prev.next = kA
                prev = kA
                kA = kA.next
            else:
                prev.next = kB
                prev = kB
                kB = kB.next
                
        if kA:
            prev.next = kA
        else:
            prev.next = kB
                
        return head
            
                
            
