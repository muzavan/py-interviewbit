class Solution:
    # @param A : integer
    # @return an integer
    dp = {}
    def climbStairs(self, A):
        if A not in self.dp:
            for i in range(1, A+1):
                if i == 1:
                    self.dp[i] = 1
                elif i == 2:
                    self.dp[i] = 2
                else:
                    self.dp[i] = self.dp[i-1] + self.dp[i-2]
                
        return self.dp[A]
