class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestSubsequenceLength(self, A):
        As = sorted(A)
        
        dprev = {}
        dnext = {}
        
        for i, a in enumerate(As):
            if i != 0:
                dprev[As[i]] = As[i-1]
                dnext[As[i-1]] = A[i]
            else:
                dprev[As[i]] = None
                
        dp = {}
        
        for a in A:
            prev = dprev[a]
            if prev is None:
                dp[a] = 1
            elif prev in dp:
                dp[a] = dp[prev] + 1
            else:
                dp[a] = 1
                
        
            
