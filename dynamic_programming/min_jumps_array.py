class Solution:
    # @param A : list of integers
    # @return an integer
    def jump(self, A):
        N = len(A)
        i, en = 0, 0
        
        jump = 0
        while True:
            if i > en:
                break
            
            if en >= N - 1:
                return jump
        
            ien = en
            while i <= ien:
                en = max(en, i + A[i])
                i += 1
                
            jump += 1
        
        return -1
        
