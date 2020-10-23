class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def threeSum(self, A):
        A = sorted(A)
        
        sols = []
        for ai in range(len(A)-2):
            a = A[ai]
            
            bi = ai + 1
            ci = len(A)-1
            
            while bi < ci:
                b = A[bi]
                c = A[ci]
                
                sm = a + b + c
                if sm == 0:
                    sols.append((a, b, c))
                    ci -= 1
                    bi += 1
                elif sm > 0:
                    ci -= 1
                else:
                    bi += 1
                
        return list(set(sols))
                
