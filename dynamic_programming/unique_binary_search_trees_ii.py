class Solution:
    # @param A : integer
    # @return an integer
    def numTrees(self, A):
        dp = {}
        res = self.solve(A, dp)
        return res
        
    def solve(self, A, dp):
        # Try recursive for now
        if A <= 1:
            return 1
        
        if A in dp:
            return dp[A]
            
        # Distribute the remaining node
        count = 0
        # We substract 1 since we already decide 1 in the node
        for i in range(A):
            l = i
            r = A - 1 - i
            
            count += (self.solve(l, dp) * self.solve(r, dp))
        
        dp[A] = count
        return count
