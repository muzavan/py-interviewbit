class Solution:
    # @param A : list of integers
    # @return an integer
    def maxp3(self, A):
        A = sorted(A)
        
        poss = []
        
        poss.append(A[-3] * A[-2] * A[-1])
        poss.append(A[0] * A[1] * A[-1])
        poss.append(A[0] * A[1] * A[2])
        
        return max(poss)
