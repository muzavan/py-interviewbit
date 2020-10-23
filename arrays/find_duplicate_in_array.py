class Solution:
    # @param A : tuple of integers
    # @return an integer
    def repeatedNumber(self, A):
        found = {k : False for k in range(1, len(A)+1)}
        for a in A:
            if found[a] :
                return a
            found[a] = True
            
        return -1
