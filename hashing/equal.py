class Solution:
    # @param A : list of integers
    # @return a list of integers
    def equal(self, A):
        i, a = 0, 0
        
        d = {}
        mn = []
        while i < len(A):
            j = i + 1
            
            while j < len(A):
                a, b = A[i], A[j]
                s = a + b
                
                if s in d:
                    p, q = d[s]
                    
                    if self.isValid(p, q, i, j):
                        mn = self.getMn(mn, (p, q, i, j))

                else:
                    d[s] = (i, j)
                    
                j += 1
                
            i += 1
            
        return mn
        
    def getMn(self, tp1, tp2):
        if len(tp1) == 0:
            return tp2
        for i, k in zip(tp1, tp2):
            if i < k:
                return tp1
                
            if i > k:
                return tp2
                
        return tp1
        
    def isValid(self, A1, B1, C1, D1):
        return (A1 < B1) and (C1 < D1) and (A1 < C1) and (B1 != D1) and (B1 != C1) 
