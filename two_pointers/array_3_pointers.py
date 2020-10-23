class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @param C : tuple of integers
    # @return an integer
    def minimize(self, A, B, C):
        ai, bi, ci = 0, 0, 0
        
        mn = max(A + B + C)
        
        while ai < len(A) and bi < len(B) and ci < len(C):
            a = A[ai]
            b = B[bi]
            c = C[ci]
            
            tmn = self.max_abs(a, b, c)
            
            if mn > tmn:
                mn = tmn
            
            rm = min([a, b, c])
            if rm == a:
                ai += 1
            elif rm == b:
                bi += 1
            else:
                ci += 1
            
        return mn
    
    def max_abs(self, a, b, c):
        return max([a, b, c]) - min([a, b, c])
    