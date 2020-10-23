class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minimumTotal(self, A):
        N = len(A)
        
        if N == 0:
            return 0
        
        dp1, dp2 =  [], []    
        for i in range(N):
            # Let's check for each index
            dp2 = []
            if i == 0:
                dp1 = A[i][:]
                continue
            
            befs = dp1
            
            M = len(befs)
            for j in range(M + 1):
                a = A[i][j]
                
                best = []
                if j != M:
                    best.append(befs[j])
                    
                if j > 0:
                    best.append(befs[j-1])
                    
                dp2.append(min(best) + a)
            
            dp1 = dp2    
            
        return min(dp1)
    
