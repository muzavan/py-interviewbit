class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sm = {0 : [-1]}
        
        ar = 0
        mx_gap = 0
        mi, mj = 0, 0
        for i, a in enumerate(A):
            ar += a
            if ar not in sm:
                sm[ar] = []
                sm[ar].append(i)
            else:
                j = sm[ar][0]
                if (i-j) > mx_gap:
                    mx_gap = i-j
                    mi = i
                    mj = j
                    
        return A[mj+1:mi+1]
                    
        
