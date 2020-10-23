class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A = sorted(A)
        target = B
        cls = None
        clsdff = None
        
        for ai in range(len(A)-2):
            bi = ai + 1
            ci = len(A)-1
            
            while bi < ci:
                a  = A[ai]
                b  = A[bi]
                c  = A[ci]
                
                sm = a + b + c
                dff = abs(sm - target)
                
                if not cls or clsdff > dff:
                    cls = sm
                    clsdff = dff
                    
                if clsdff == 0:
                    return cls
                    
                if sm > target:
                    ci -= 1
                elif sm < target:
                    bi += 1
                    
        return cls
                
            
