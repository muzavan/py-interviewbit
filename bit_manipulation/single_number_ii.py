class Solution:
    # @param A : tuple of integers
    # @return an integer
    def singleNumber(self, A):
        ones = 0
        twos = 0
        
        for a in A:
            twos = twos | (ones & a)
            ones = ones ^ a
            
            cmb = ~(ones & twos)
            
            ones &= cmb
            twos &= cmb
            
        return ones
            
            
