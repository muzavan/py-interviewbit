class Solution:
    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        dp = {}
        for a in A:
            if a not in dp:
                dp[a] = 0
                
            dp[a] += 1
            
        mx = 0
        imx = 0
        
        for k, v in dp.items():
            if v > mx:
                mx = v
                imx = k
        
        
        return imx
