class Solution:
    # @param A : integer
    # @return a list of strings
    def generateParenthesis(self, A):
        return self.getParenth("", A, 0)
        
        
    def getParenth(self, pre, L, R):
        if L == 0 and R == 0:
            return [pre]
            
        res = []
        if L > 0:
            pr = pre + "("
            res.extend(self.getParenth(pr, L-1, R+1))
            
        if R > 0:
            pr = pre + ")"
            res.extend(self.getParenth(pr, L, R-1))
            
        return res
            
        
        
            
        
            
        
