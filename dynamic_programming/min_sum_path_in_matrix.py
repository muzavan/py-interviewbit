class Solution:
    # @param A : list of list of integers
    # @return an integer
    def minPathSum(self, A):
        dp = {}
        
        nR = len(A)
        nC = len(A[0])
        
        for i in range(nR):
            for j in range(nC):
                bestScore = []
                if i != 0:
                    bestScore.append(A[i][j] + dp[(i-1, j)])
                if j != 0:
                    bestScore.append(A[i][j] + dp[(i, j-1)])
                if i == 0 and j == 0:
                    bestScore.append(A[i][j])
                    
                mn = min(bestScore)
                dp[(i, j)] = mn
                
        return dp[(nR-1, nC-1)]
