class Solution:
    # @param A : unsigned integer
    # @return an unsigned integer
    def reverse(self, A):
        B = 0
        N_BIT = 32
        for n in range(N_BIT):
            b = (A>>n) & 1
            B = (B<<1) ^ b
            
        return B
