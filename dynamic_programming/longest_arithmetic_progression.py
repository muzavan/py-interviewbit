class Solution:
    # @param A : tuple of integers
    # @return an integer
    def solve(self, A):
        dp = {}
        N = len(A)
        
        if N <= 1:
            return N
        
        Arev = {}
        mx = 0
        
        for i, a in enumerate(A):
            if a not in Arev:
                Arev[a] = []
            Arev[a].append(i)
        
        for i in range(N):
            dp[i] = {}
            dp[i][i] = 1
            for j in range(i+1, N):
                dp[i][j] = 2
                
                need = (2 * A[i]) - A[j]
                if need in Arev:
                    pos = 0
                    for k in Arev[need]:
                        if k >= i:
                            break
                        pos = k
                
                    dp[i][j] = max(dp[i][j], dp[pos][i] + 1)
                    
                mx = max(dp[i][j], mx)
                
        return mx