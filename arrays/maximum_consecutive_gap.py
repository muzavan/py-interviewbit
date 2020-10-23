class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        A = sorted(A)
        res = 0
        for idx in range(len(A)):
            if idx == len(A)-1:
                break
            diff = A[idx] - A[idx+1] if A[idx] > A[idx+1] else A[idx+1] - A[idx]
            res = res if res > diff else diff
            
        return res