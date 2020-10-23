class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def uniquePaths(self, A, B):
        mults = [m for m in range(A+1, A+B+1)]
        divs = [b for b in range(2,B+1)]
        
        result = 1
        for m in mults:
            result *= m
            
        for d in divs:
            result /= d
            
        return result
        
