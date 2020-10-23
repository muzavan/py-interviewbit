class Solution:
    # @param A : list of integers
    # @return A after the sort
    def sortColors(self, A):
        ni = 0
        nj = 0
        nk = 0
        
        for a in A:
            if a == 0:
                ni += 1
            elif a == 1:
                nj += 1
            else:
                nk += 1
                
        A = [0] * ni + [1] * nj + [2] * nk
        return A
