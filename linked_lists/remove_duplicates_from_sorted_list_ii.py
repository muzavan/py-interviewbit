# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        head = A
        dups = set()
        prevK = None
        K = A
        while K:
            if prevK and prevK.val == K.val and prevK.val not in dups:
                dups.add(prevK.val)
                
            prevK = K
            K = K.next
            
        while head and head.val in dups:
            head = head.next
            
        prevK = head
        
        if prevK:
            K = head.next
            
            while K:
                while K and K.val in dups:
                    K = K.next
                    
                prevK.next = K
                prevK = K
                if K:
                    K = K.next
        
        return head
