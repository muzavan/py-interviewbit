# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        prep = None
        appn = None
        head = A
        m = B
        n = C
        
        if m == 1:
            K = A
            while n > 1:
                K = K.next
                n -= 1
                
            head = K
            n = C
            
        mK = A
        
        while m > 1:
            prep = mK
            mK = mK.next
            m -= 1
           
        nK = A 
        while n > 1:
            nK = nK.next
            n -= 1
            
        appn = nK.next
        nK.next = None
        
        self.reverseList(mK, prep, appn)
        return head
    
    def reverseList(self, A, prepend, append):
        rA = self.reverseAllList(A)
        
        if prepend:
            prepend.next = rA
        A.next = append
    
    def reverseAllList(self, A):
        prev = None
        K = A
        
        while K:
            nxt = K.next
            K.next = prev
            prev = K
            K = nxt
            
        return prev
    
    
