from math import log
from math import sqrt

class Solution:
    # @param A : integer
    # @return an integer
    def isPower(self, A):
        if A == 1:
            return 1
        N = int(sqrt(A))
        for a in range(2, N+1):
            if self.isPerfectPower(A, a):
                return 1
                
            
        return 0
        
    def isPerfectPower(self, A, a):
        t = A
        while(t > 1):
            t = t / a
            
        return t == 1
