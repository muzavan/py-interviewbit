class Solution:
    # @param A : integer
    # @return a strings
    def convertToTitle(self, A):
        numToChar = self.numToChar
        res = []
        k = A
        while (k > 26):
            p = k % 26
            p = p if p != 0 else 26
            k = k // 26
            k = k if p != 26 else k-1
            res.append(numToChar(p))
        
        res.append(numToChar(k))
        res.reverse()
        return "".join([r for r in res])
    
    def numToChar(self, a):
        k = a + 64
        return chr(k)