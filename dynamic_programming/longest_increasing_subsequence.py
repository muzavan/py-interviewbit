class Solution:
    # @param A : tuple of integers
    # @return an integer
    def lis(self, A):
        dp = {}
        
        for a in A:
            ks = dp.keys()
            
            prev = 0
            for k in ks:
                if k < a:
                    prev = max(prev, dp[k])
                    
            if a not in dp:
                dp[a] = 1
                
            curr = prev + 1
            
            dp[a] = max(dp[a], curr)
            
        
        return max([v for k, v in dp.items()])