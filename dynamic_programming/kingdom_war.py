class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        N = len(A)
        if N == 0:
            return 0
            
        M = len(A[0])
        
        dp = {} # store the max sum from i, j to N-1, M-1
        
        mx = -201
        for i in range(N-1, -1, -1):
            dp[i] = {}
            for j in range(M-1, -1, -1):
                curr = A[i][j]
                bestScores = [curr]
                
                if i != N-1:
                    bestScores.append(curr + dp[i+1][j])
                if j != M-1:
                    bestScores.append(curr + dp[i][j+1])
                if i != N-1 and j != M - 1:
                    bestScores.append(curr + dp[i][j+1] + dp[i+1][j] - dp[i+1][j+1])
                    
                best = max(bestScores)
                dp[i][j] = best
                mx = max(mx, best)
            
            if (i+1) in dp:
                del dp[i+1]
        
        # for i in range(N):
        #     r = []
        #     for j in range(M):
        #         r.append(dp[(i, j)])
                
        #     print(r)
        return mx
