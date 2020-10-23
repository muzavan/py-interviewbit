# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return the head node in the linked list
    def deleteDuplicates(self, A):
        K = A
        prevK = None
        
        while K:
            if prevK and prevK.val == K.val:
                prevK.next = K.next
            else:
                prevK = K
                
            K = K.next
            
        return A
