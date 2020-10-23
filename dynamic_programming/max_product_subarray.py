from functools import reduce

class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProduct(self, A):
        # If there is no 0 or -, the maximum would
        # be the whole array
        
        lA = len(A)
        
        if not lA:
            return 0
            
        res = []
        max_neg = A[0] 
        max_pos = A[0] if A[0] > 0 else None
        
        for a in A[1:]:
            if a == 0:
                res.append(0)
                if max_pos is not None:
                    res.append(max_pos)
                    
                if max_neg is not None:
                    res.append(max_neg)
                
                max_pos, max_neg = None, None
                continue
            
            if a < 0:
                if max_pos:
                    res.append(max_pos)
                    max_pos = None
                    
                max_neg = max_neg * a if max_neg else a
                if max_neg > 0:
                    max_pos = max_neg
                continue
            
            max_pos = max_pos * a if max_pos else a
            max_neg = max_neg * a if max_neg else a
        
        if max_pos is not None:
            res.append(max_pos)
            
        if max_neg is not None:
            res.append(max_neg)
            
        # print(res)
        return max(res)
            
