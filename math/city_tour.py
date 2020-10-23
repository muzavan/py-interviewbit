class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    
    def solve(self, A, B):
        Bs = sorted(B)
        
        mids = []
        for i, b in enumerate(Bs):
            if i == 0:
                mids.append(b-1)
                
            if i >= 1:
                mids.append(b-Bs[i-1]-1)
                
            if i == len(B)-1:
                mids.append(A-b)
        
        tot = sum(mids)
        
        divised = [t for t in range(tot,0,-1)]
        divisor = []
        for m in mids:
            if m == 0 or m == 1:
                continue
            
            divisor.extend([t for t in range(m,0,-1)])
        
        times = sum(mids[1:-1]) - sum([1 for m in mids[1:-1] if m != 0])
        
        # print(mids)
        # print(divised, divisor, times)
        return self.combine(divised, divisor, times)
    
    def combine(self, divised, divisor, times):
        ds = divisor[:-1]
        for d in ds:
            if d in divised:
                divised.remove(d)
                divisor.remove(d)
                
        res = 1
        for d in divised:
            res *= d
            
        for d in divisor:
            res /= d
            
        for _ in range(times):
            res *= 2
                
        return res % (1000000007)
    
                
                
    
    
            
