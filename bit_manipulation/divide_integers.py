class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def divide(self, A, B):
        res = 0
        negative = False
        
        if A < 0:
            A = 0 - A
            negative = not negative
            
        if B < 0:
            B = 0 - B
            negative = not negative
            
            
        while(A >= B):
            res += 1
            A -= B
            
        if negative:
            res = 0 - res
            
        if res < -2147483648 or res > 2147483647:
            res = 2147483647
            
        return res
