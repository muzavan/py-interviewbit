class Solution:
    # @param A : list of integers
    # @return an integer
    def nTriang(self, A):
        A = sorted(A)
        
        n = 0
        for ci in range(len(A)-1,1,-1):
            c = A[ci]
            
            ai = 0
            bi = ci-1
            
            while ai < bi:
                a, b = A[ai], A[bi]
                if (a + b) > c:
                    n += (bi-ai)
                    bi -= 1
                else:
                    ai += 1
            
        return int(n%(1e9+7))
