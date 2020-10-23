class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    def fourSum(self, A, B):
        A = sorted(A)        
        # Find couple combination:
        d = {}
        for i, a in enumerate(A):
            
            j = i + 1
            
            while j < len(A):
                aa = A[j]
                s = a + aa
                if s not in d:
                    d[s] = []
                    
                d[s].append([i, j])
                j += 1
                
        
        # Find pair
        ress = set()
        prosk = set()
        for k in sorted(list(d.keys())):
            r = B - k
            
            if r in prosk:
                continue
            if r in d:
                ks = d[k]
                rs = d[r]
                for _k in ks:
                    for _r in rs:
                        if (_k[0] < _r[0]) and (_r[0] != _k[1]) and (_k[1] < _r[1]):
                            v, w, x, y = A[_k[0]], A[_k[1]], A[_r[0]], A[_r[1]]
                            q = sorted([v, w, x, y])
                            ress.add(tuple(q))
                            
            prosk.add(k)
                
        return sorted(list(ress))       
            
