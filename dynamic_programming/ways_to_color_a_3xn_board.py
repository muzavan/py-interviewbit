MOD = 10**9 + 7

class Solution:
    # @param A : integer
    # @return an integer
    def __init__(self):
        pass
        # W(n+1) = 10*Y(n)+11*W(n);
        # Y(n+1) = 7*Y(n)+5*W(n);
    
    def solve(self, A):
        color2 = 12
        color3 = 24
            
        for _ in range(2, A+1):
            tcolor3 = ((10*color2) + (11*color3)) % MOD
            tcolor2 = ((7*color2) + (5*color3)) % MOD
            
            color2, color3 = tcolor2, tcolor3
            
        return (color2 + color3) % MOD
    
