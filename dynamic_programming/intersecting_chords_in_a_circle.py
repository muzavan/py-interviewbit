MOD = 10**9 + 7

class Solution:
    # @param A : integer
    # @return an integer
    def chordCnt(self, A):
        return self.chordPossible(2 * A) % MOD
        
    def chordPossible(self, n):
        # Traversal
        dp = [1]
        for a in range(1, n+1):
            if a % 2 == 1:
                dp.append(0)
                continue
            
            sm = 0
            for k in range(a):
                l = k
                r = a - 2 - k
                sm = sm + (dp[l] * dp[r])
                
            dp.append(sm)
            
        return dp[n]
