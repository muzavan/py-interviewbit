class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        mn = min(B)
        idx = 0
        for i, b in enumerate(B):
            if b == mn:
                idx = i
                break
            
        N = A / int(mn)
        res = [idx] * N
        sm = mn * N
        
        ri = 0
        for i, b in enumerate(B):
            if ri >= len(res):
                break
            
            r = res[ri]
            if i >= r:
                break
            
            tsm = sm - B[r] + b
            if tsm > A:
                continue
            
            while tsm <= A:
                res[ri] = i
                sm = tsm
                ri += 1
                
                if ri >= len(res):
                    break
                r = res[ri]
                tsm = sm - B[r] + b
     
        return res
