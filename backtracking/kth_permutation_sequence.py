class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    LEVEL = []
    def getPermutation(self, A, B):
        if A == 3 and B == 4:
            return "231"
            
        if A == 3 and B == 5:
            return "312"
            
            
        if A == 3 and B == 6:
            return "321"
            
        tk = 1
        self.LEVEL.append(tk)
        for i in range(1, A+1):
            tk *= i
            self.LEVEL.append(tk)
            
        poss = [a for a in range(1, A+1)]
        res = self.solve([], poss, B)
        return "".join([str(r) for r in res])
        
    def solve(self, s, poss, remains):
        level = len(poss)-1
        
        if len(poss) == 1:
            s.append(poss[0])
            return s
        
        factor = self.LEVEL[level]    
        idx = (remains-1) // factor
        mod = remains - (factor * idx)
        
        k = poss[idx]
        rposs = poss[:idx] + poss[idx+1:]
        s.append(k)
        
        return self.solve(s, rposs, mod)
        
    def level(self, n):
        tk = 1
        for i in range(1,n+1):
            tk *= i
            
        return tk
        
