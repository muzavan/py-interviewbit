class Solution:
    # @param A : string
    # @return an integer
    def titleToNumber(self, A):
        l = len(A)
        total = self.charToNum(A[0])
        for a in range(1,l):
            total *= 26
            total += self.charToNum(A[a])
        return total
    
    def charToNum(self, a):
        k = ord(a)
        return k - 64