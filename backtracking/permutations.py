class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def permute(self, A):
        A = sorted(A)
        return self.solve([], A)
        
    def solve(self, pre, A):
        res = []
        if len(A) == 0:
            return [pre]
        
        for i, el in enumerate(A):
            currA = A[:i] + A[i+1:]
            res.extend(self.solve(pre + [el], currA))
            
        return res
            
