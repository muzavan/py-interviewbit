class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def rodCut(self, A, B):
        NB = [0]
        NB.extend(B)
        NB.append(A)
        
        _, ar = self.minCut({}, NB)
        return ar
        
    def minCut(self, dp, B):
        if len(B) == 2:
            return 0, []
            
        if (B[0], B[-1]) in dp:
            return dp[(B[0], B[-1])]
            
        ln = B[-1] - B[0]
        
        pos = []
        for pi in range(1, len(B)-1):
            t1, n1 = self.minCut(dp, B[:pi+1])
            t2, n2 = self.minCut(dp, B[pi:])
            pos.append((ln + t1 + t2, [B[pi]] + n1 + n2))
        
        pos = sorted(pos)
        dp[(B[0], B[-1])] = pos[0]
        return pos[0]
        
