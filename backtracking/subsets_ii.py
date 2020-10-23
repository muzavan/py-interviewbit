class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsetsWithDup(self, A):
        A = sorted(A)
        
        prepend = []
        
        return self.asubset(prepend, A)
    
    
    def asubset(self, prepend, A):
        ai = 0
        result = [prepend]
        prev = None
        
        while ai < len(A):
            a = A[ai]
            if not prev or a != prev:
                xprepend = prepend + [a]
                result.extend(self.asubset(xprepend, A[ai+1:]))
            prev = a
            ai += 1
            
        return result
        
