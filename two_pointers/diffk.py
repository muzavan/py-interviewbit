class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        if B == 0:
            return 0 if len(A) == len(set(A)) else 1
            
        As = set([a + B for a in A])
        
        for a in A:
            if a in As:
                return 1
                
        return 0
        
        
        
