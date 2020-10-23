class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        res = self.solve(["0", "1"], A)
        return [int(r, 2) for r in res]
        
    def solve(self, pre, A):
        if A == 1:
            return pre
            
        G = ["0{}".format(p) for p in pre]
        R = ["1{}".format(p) for p in pre[::-1]]
        
        return self.solve(G+R, A-1)