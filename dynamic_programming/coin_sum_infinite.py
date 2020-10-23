class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def coinchange2(self, A, B):
        dp = [0] * (B + 1)
        dp[0] = 1
        
        for coin in A:
            for i in range(1, B + 1):
                if coin <= i:
                    dp[i] = dp[i] + dp[i - coin]
        return dp[-1] % 1000007