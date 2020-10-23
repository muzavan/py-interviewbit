class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def slidingMaximum(self, A, B):
        qs = []
        res = []
        
        if B > len(A):
            B = len(A)
            
        j = 0
        while j < B - 1:
            a = A[j]
            if len(qs) == 0:
                qs.append(j)
            else:
                k = 0
                while k < len(qs):
                    if a > A[qs[k]]:
                        qs = qs[:k] + [j]
                        break
                    k += 1
                    
                if k == len(qs) and k < B:
                    qs.append(j)
                    
            j += 1
            
        while j < len(A):
            a = A[j]
            if len(qs) > 0 and j - B + 1 > qs[0]:
                qs.pop(0)
                
            if len(qs) == 0:
                qs.append(j)
            else:
                k = 0
                while k < len(qs):
                    if a > A[qs[k]]:
                        qs = qs[:k] + [j]
                        break
                    k += 1
                    
                if k == len(qs) and k < B:
                    qs.append(j)
                    
            # print(j, qs)
            mx = A[qs[0]]
            
            j += 1
            res.append(mx)
        
        return res
