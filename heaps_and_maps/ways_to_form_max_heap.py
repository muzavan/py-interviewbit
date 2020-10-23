MOD = 10**9+7

class Solution:
    # @param A : integer
    # @return an integer
    
    def comb(self,r,n) :
        if 2*r > n : 
            return self.comb(n-r,n)
        c = 1
        for i in range(r) :
            c = c*(n-i)//(i+1)
        return c
    
    def solve(self, A):
        ans,h = [1,1], 0
        for n in range(2,A+1) :
            if 2<<h <= n :
                h += 1
            m = n-(1<<h)+1
            l = (1<<(h-1))-1 + min(m,1<<(h-1))
            r = (1<<(h-1))-1 + max(0,m-(1<<(h-1)))
            ans.append((self.comb(l,n-1)*ans[l]*ans[r])%MOD)
        return ans[A]