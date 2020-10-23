class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def order(self, A, B):
        d = {}
        for a, b in zip(A, B):
            d[a] = b
        
        As = sorted(A)
        
        res = [None] * len(As)
        idxs = [i for i in range(len(As))]
        
        i = 0
        while i < len(As):
            v = As[i]
            idx = d[v]
            k = idxs.pop(idx)
            res[k] = v
            i += 1
        
        return res
            
        
        
