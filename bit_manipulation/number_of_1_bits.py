class Solution:
    # @param A : integer
    # @return an integer
    def numSetBits(self, A):
        n = A
        if n < 2:
            return n
            
        tot = 1
        while (n >= 2):
            tot += (n%2)
            n /= 2
        
        return tot
