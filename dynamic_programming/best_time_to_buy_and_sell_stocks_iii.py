class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):
        nA = len(A)
        if nA <= 1:
            return 0
            
        mxs = [0]
        bought = A[0]
        mx = 0
        for a in A:
            mxs.append(mx)
            if a < bought:
                bought = a
            else:
                mx = max(mx, a - bought)
        
        mx = 0     
        sold = A[-1]
        for i in range(nA-2, -1, -1):
            a = A[i]
            
            if a > sold:
                sold = a
            else:
                currProfit = mxs[i] + (sold - a)
                mx = max(mx, currProfit)
        return mx
            
        
