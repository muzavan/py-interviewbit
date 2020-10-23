class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        jump = int(len(A)) / 3
        tjump = len(A) - jump
        
        sA = sorted(A)
        for i in range(tjump):
            j = i + jump
            if sA[i] == sA[j]:
                return sA[i]
            
        return -1
        
        
