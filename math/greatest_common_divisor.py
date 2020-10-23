class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):
        if A < B:
            return self.gcd(B, A)
            
        if A%B == 0:
            return B
            
        nextA = B
        nextB = A%B
        
        return self.gcd(nextA, nextB)
