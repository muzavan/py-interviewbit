INF = float('inf')

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def solve(self, A, B, C):
        dp = [INF] * (1001 + 1)
        
        for b, c in zip(B, C):
            dp[b] = min(dp[b], c)
        
        for a in range(1, 1001+1):
            for k in range(1, (a // 2) + 1):
                dp[a] = min(dp[a], dp[a-k] + dp[k])
        
        return sum([dp[a] for a in A])
