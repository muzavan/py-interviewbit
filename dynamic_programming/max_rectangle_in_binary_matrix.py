from collections import defaultdict

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def maximalRectangle(self, A):
        dp = {}
        
        R = len(A)
        
        if R == 0:
            return 0
            
        C = len(A[0])
        
        
        for r in range(R):
            dp[r] = {}
            for c in range(C):
                a = A[r][c]
                
                if c == 0:
                    dp[r][c] = a
                    continue
                
                if a == 0:
                    dp[r][c] = 0
                    continue
                
                dp[r][c] = dp[r][c-1] + 1
        
        mx = 0
        mxs = defaultdict(dict)
        for r in range(R):
            for c in range(C):
                d = dp[r][c]
                h = 1
                
                tmx = d * h
                for rr in range(r+1, R):
                    dd = dp[rr][c]
                    
                    if dd == 0:
                        break
                    
                    h += 1
                    d = min(d, dd)
                    
                    tmx = max(tmx, d * h)
                
                mx = max(mx, tmx)    
                mxs[r][c] = tmx
        
        
        # for r in range(R):
        #     row = []
        #     for c in range(C):
        #         row.append(dp[r][c])
                
        #     print(row)
        
        # print("MXS")    
        # for r in range(R):
        #     row = []
        #     for c in range(C):
        #         row.append(mxs[r][c])
                
        #     print(row)
        return mx