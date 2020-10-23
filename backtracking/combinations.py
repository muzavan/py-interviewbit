class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of list of integers
    def combine(self, A, B):
        return self.tcombine([], list(range(1, A+1)), B)
    
    def tcombine(self, pre, A, n):
        res = []
        if n == 1:
            for a in A:
                res.append(pre + [a])
               
            return res
            
        ai = 0
        
        while ai < len(A):
            a = A[ai]
            B = A[ai+1:]
            
            res.extend(self.tcombine(pre+[a], B, n-1))
            ai += 1
            
        return res
        
