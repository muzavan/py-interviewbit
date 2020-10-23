class Solution:
    # @param A : string
    # @param B : integer
    # @return an integer
    # The idea is to either split the stable or add it to current one
    def arrange(self, A, B):
        stables = A
        K = B
        
        if K > len(stables) or K == 0:
            return -1
            
        return self.solve(stables, K, {})
    
    def translate(self, stables):
        tr = ""
        for s in stables:
            if s == 'W':
                tr += 'B'
            else:
                tr += 'W'
                
        return tr
        
    def solve(self, stables, K, dp):
        if (stables, K) in dp:
            return dp[(stables, K)]
            
        tr = self.translate(stables)
        
        if (tr, K) in dp:
            return dp[(tr, K)]
        
        if K == 1:
            return self.calculateScore(stables)
    
        if len(stables) == K:
            return 0
            
        minScore = min([self.calculateScore(stables[:i]) for i in range(1, len(stables)-K + 2)])
        
        dp[(stables, K)] = minScore
        return minScore
    
    def calculateScore(self, stables):
        n = len(stables)
        nB = stables.count('B')
        
        return (n - nB) * nB