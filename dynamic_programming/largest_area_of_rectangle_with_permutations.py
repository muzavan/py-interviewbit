class Solution:
    # @param A : list of list of integers
    # @return an integer
    def solve(self, A):
        R = len(A)
        if R == 0:
            return 0
            
        C = len(A[0])
        
        hist = []
        for _ in range(R):
            h = []
            for _ in range(C):
                h.append(0)
            hist.append(h)
        
        ci = 0
        while ci < C:
            ri = 0
            pre = 0
            while ri < R:
                a = A[ri][ci]
                if a == 1:
                    pre += 1
                    hist[ri][ci] = pre
                else:
                    pre = 0
                
                ri += 1
            
            ci += 1
            
        ri = 0
        
        # Sort based on non increasing manner
        mx = 0
        while ri < R:
            hist[ri] = sorted(hist[ri], reverse=True)
            ss = hist[ri]
            ci = 0
            
            while ci < C and ss[ci] != 0:
                area = (ci+1) * ss[ci]
                mx = max(mx, area)
                ci += 1
             
            ri += 1
            
        # print(hist)
        return mx
