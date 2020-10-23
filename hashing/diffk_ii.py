class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def diffPossible(self, A, B):
        k = set()
        for a in A:
            a2 = B + a
            if a2 in k:
                return 1
                
            k.add(a)
            
        return 0
