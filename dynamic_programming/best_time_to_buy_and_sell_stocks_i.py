MN = 10**7 + 1

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        L = len(A)
        
        if L <= 1:
            return 0
            
        mx = 0
        mn = A[0]
        
        for a in A[1:]:
            mx = max(a-mn, mx)
            mn = min(a, mn)
        
        return mx
            
            
