class Solution:
    # @param A : list of list of integers
    # @return the same list modified
    def rotate(self, A):
        n = len(A[0])
        
        B = []
        for i in range(n):
            C = []
            for j in range(n-1,-1,-1):
                C.append(A[j][i])
                
            B.append(C)
            
        return B
