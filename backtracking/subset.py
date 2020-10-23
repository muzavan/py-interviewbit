class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A = sorted(A)
        
        prepend = []
        
        return self.asubset(prepend, A)
    
    
    def asubset(self, prepend, A):
        ai = 0
        result = [prepend]
        
        while ai < len(A):
            a = A[ai]
            xprepend = prepend + [a]
            result.extend(self.asubset(xprepend, A[ai+1:]))
            ai += 1
            
        return result
        
