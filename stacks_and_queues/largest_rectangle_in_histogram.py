class Solution:
    # @param A : list of integers
    # @return an integer
    def largestRectangleArea(self, A):
        mx = 0
        lmx = []
        i = 0
        while i < len(A):
            a = A[i]
            if len(lmx) == 0 or a >= A[lmx[-1]]:
                lmx.append(i)
                i += 1
                continue
            
            while len(lmx) > 0 and A[lmx[-1]] > a:
                h = A[lmx.pop(-1)]
                p = (i-lmx[-1]-1) if len(lmx) > 0 else i
                mx = max(mx, h*p)
                
            lmx.append(i)
            i += 1
            
        while len(lmx) > 0:
            h = A[lmx.pop(-1)]
            p = (i-lmx[-1]-1) if len(lmx) > 0 else i
            mx = max(mx, h*p)
        return mx
    
