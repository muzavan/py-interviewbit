def moveFunc(r, c):
    def move(x, y):
        return x+r, y+c
        
    return move

DIRECTION = {
    "U" : moveFunc(-1, 0),
    "D": moveFunc(1, 0),
    "L": moveFunc(0, -1),
    "R": moveFunc(0, 1),
    "LU": moveFunc(-1, -1),
    "LD": moveFunc(1, -1),
    "RU": moveFunc(-1, 1),
    "RD": moveFunc(1, 1),
}


class Solution:
    # @param A : list of strings
    # @return a list of list of integers
    def queenAttack(self, A):
        R = len(A)
        C = len(A[0])
        
        dp = {}
        for r in range(R):
            dp[r] = {}
            for c in range(C):
                dp[r][c] = 0
            
        for r in range(R):
            for c in range(C):
                a = A[r][c]
                
                if a == '1':
                    fill(A, r-1,c, R, C, dp, "U")
                    fill(A, r+1,c, R, C, dp, "D")
                    fill(A, r,c-1, R, C, dp, "L")
                    fill(A, r,c+1, R, C, dp, "R")
                    fill(A, r-1,c-1, R, C, dp, "LU")
                    fill(A, r+1,c-1, R, C, dp, "LD")
                    fill(A, r-1,c+1, R, C, dp, "RU")
                    fill(A, r+1,c+1, R, C, dp, "RD")
        
        res = []            
        for r in range(R):
            rs = []
            for c in range(C):
                rs.append(dp[r][c])
                
            res.append(rs)
                

        return res
        
        
    
    
def fill(A, r, c, R, C, res, D):
    if r < 0 or r >= R or c < 0 or c >= C:
        return
    
    res[r][c] = 1 + res[r][c]
    
    
    if A[r][c] != '1':
        r, c = DIRECTION[D](r, c)
        fill(A, r, c, R, C, res, D)
    
    
    
    
    

