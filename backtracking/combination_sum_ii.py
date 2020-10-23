class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def combinationSum(self, A, B):
        A = sorted(A)
         
        return self.findCombination([], A, B)
     
     
    def findCombination(self, pre, A, N):
        res = []
        ai = 0
        prev = None
        while ai < len(A) and A[ai] <= N:
            if not prev or A[ai] != prev:
                if A[ai] == N:
                    res.append(pre + [A[ai]])
                else:
                    tmp = self.findCombination(pre+[A[ai]], A[ai+1:], N-A[ai])
                    res.extend(tmp)
                     
                prev = A[ai]
            ai += 1
 
        return res
