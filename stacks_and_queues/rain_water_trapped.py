class Solution:
    # @param A : tuple of integers
    # @return an integer
    def trap(self, A):
        na = len(A)
        
        ls = [0] * na
        rs = [0] * na
        
        
        ls[0] = A[0]
        
        for i in range(1, na):
            a1 = ls[i-1]
            a2 = A[i]
            
            ls[i] = a1 if a1 > a2 else a2
            
        rs[-1] = A[-1]
        for i in range(na-2, -1, -1):
            a1 = rs[i+1]
            a2 = A[i]
            
            rs[i] = a1 if a1 > a2 else a2
            
        tot = 0
        
        for a, l, r in zip(A, ls, rs):
            tot += (min(l,r) - a)
            
        return tot
            
        
        
