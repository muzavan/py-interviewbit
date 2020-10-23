class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        c = 0
        for a in A:
            c = c ^ a
        return c
    
    
