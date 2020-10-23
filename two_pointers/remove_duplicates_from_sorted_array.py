class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        na = len(A)
        ai = 0
        cnt = 1
        aj = 1
        
        if na == 1:
            return 1
            
        prev = A[ai]
        while aj < na:
            a = A[aj]
            if a != prev:
                A[cnt] = a
                prev = a
                cnt += 1
                
            aj += 1
            
        return cnt
        
