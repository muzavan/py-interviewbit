MOD = 10000003
class Solution:
    # @param A : string
    # @return an integer
    def seats(self, A):
        return self.solve(A)
    
    def solve(self, A):
        occ = [i for i, a in enumerate(A) if a == 'x']
        
        no = len(occ)
        
        if no <= 1:
            return 0
        
        mid = no // 2
        med = occ[mid]
        final = list(range(med - mid, med + mid + 1))
        if no % 2 == 0:
            med = (occ[mid] + occ[mid-1]) // 2
            final = list(range(med - mid + 1, med + mid + 1))
        
        cnt = 0    
        for o, i in zip(occ, final):
            cnt += abs(o - i)
            cnt %= MOD
            
        return cnt
            
