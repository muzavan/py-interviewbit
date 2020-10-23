class Solution:
    # @param A : list of integers
    # @return an integer
    def candy(self, A):
        N = len(A)
        candysLeft = [1] * N
        candysRight = [1] * N
        li = 1
        
        while li < N:
            if A[li] > A[li-1]:
                candysLeft[li] = candysLeft[li-1] + 1 
            li += 1
            
        ri = N - 2
        while ri >= 0:
            if A[ri] > A[ri+1]:
                candysRight[ri] = candysRight[ri+1] + 1
            ri -= 1
              
        sm = 0
        for l, r in zip(candysLeft, candysRight):
            sm += max(l, r)
        return sm
