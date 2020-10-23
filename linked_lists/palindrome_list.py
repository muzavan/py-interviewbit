# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param A : head node of linked list
    # @return an integer
    def lPalin(self, A):
        lA = self.getLen(A)
        odd = False
        
        # print(lA)
        
        if lA % 2 ==  1:
            odd = True
            
        lIter = lA/2
        
        stk = []
        
        # print(A.val)
        for _ in range(lIter):
            stk.append(A.val)
            A = A.next
            
        # print(A.val, stk)
        if odd:
            A = A.next
            
        while A:
            s = stk.pop(-1)
            if A.val != s:
                return 0
            A = A.next
                
        return 1
    
    def getLen(self, A):
        K = A
        n = 0
        while K:
            K = K.next
            n += 1
            
        return n
