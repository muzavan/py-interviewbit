class Solution:
    # @param A : list of integers
    # @return an integer
    def findMinXor(self, A):
        if len(A) == 1:
            return A[0]
            
        A = sorted(A)
        mn = A[-1] ^ A[0]
        i = 0
        while(i < len(A)-1):
            tmp = A[i+1] ^ A[i]
            mn = mn if tmp > mn else tmp
            i += 1
            
        return mn
            
