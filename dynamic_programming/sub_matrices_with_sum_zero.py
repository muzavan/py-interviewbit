class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        R, C = len(A), len(A[0]) if len(A) > 0 else 0
        
        if not (R and C):
            return 0
            
        dp = {} # dp[(i,j)] is sum of submatrix (0,0) to (i, j)
        
        for r in range(R):
            for c in range(C):
                sm = A[r][c]
                
                if r != 0 and c != 0:
                    sm += dp[(r-1,c)]
                    sm += dp[(r, c-1)]
                    sm -= dp[(r-1, c-1)]
                    
                elif r != 0:
                    sm += dp[(r-1, c)]
                elif c != 0:
                    sm += dp[(r, c-1)]
                    
                dp[(r, c)] = sm
                
        cnt = 0
        for r1 in range(R):
            for r2 in range(r1, R):
                prev_sum = {0: 1}
                for c in range(C):
                    sm = dp[(r2, c)]
                    
                    if r1 != 0:
                        sm -= dp[(r1-1, c)]
                        
                    if sm in prev_sum:
                        cnt += prev_sum[sm]
                    else:
                        prev_sum[sm] = 0
                        
                    prev_sum[sm] += 1
                        
                
        return cnt
