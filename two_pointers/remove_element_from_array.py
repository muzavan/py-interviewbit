class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def removeElement(self, A, B):
        i, j = 0, 0
        na = len(A)
        
        while j < na:
            a = A[j]
            if a != B:
                A[i] = a
                i += 1
                
            j += 1
            
            
        return i
