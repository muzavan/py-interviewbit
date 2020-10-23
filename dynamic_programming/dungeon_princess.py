class Solution:
    # @param A : list of list of integers
    # @return an integer
    def calculateMinimumHP(self, A):
        dp = {}
        
        # Best way to certain point,
        # Is the way with the minimal health needed
        # To get a certain point
        
        N = len(A)
        if N == 0:
            return 0
        M = len(A[0])
        
        for i in range(N-1, -1, -1):
            dp[i] = {}
            for j in range(M-1, -1, -1):
                a = A[i][j]
                
                if i == N-1 and j == M-1:
                    if a > 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = 1 - a
                        
                    continue
                
                minScore = []
                
                if i != N - 1:
                    minScore.append(dp[i+1][j])
                
                if j != M - 1:
                    minScore.append(dp[i][j+1])
                    
                # If dp is defined, it means that
                # that particular path alread know
                # how to reach bottom right
                
                mn = min(minScore)
                
                if 1 + a >= mn:
                    dp[i][j] = 1
                else:
                    dp[i][j] = mn - a
                    
            if (i + 1) in dp:
                del dp[i+1]
            
        
        # print("A")
        # for i in range(N):
        #     print(A[i])
            
        # print("DP")
        # for i in range(N):
        #     r = []
        #     for j in range(M):
        #         r.append(dp[i][j])
                
        #     print(r)
        
        return dp[0][0]
                
        
