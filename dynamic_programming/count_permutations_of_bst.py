MOD = 10**9 + 7

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def cntPermBST(self, A, B):
        dp = {}
        return self.countPermutation(A, B, dp)
        
        
    def countPermutation(self, A, B, dp):
        if A <= 1:
            if B == 0:
                return 1
            return 0
            
        if (A, B) in dp:
            return dp[(A, B)]
            
        cnt = 0
        
        for i in range(A):
            l = i
            r = A - 1 - i
            
            ret = 0
            
            # Count the combination
            p1 = self.countPermutation(r, B - 1, dp)
            
            if p1 != 0:
                for j in range(B-1):
                    ret += (self.countPermutation(l, j, dp) * p1)
            
            p2 = self.countPermutation(l, B - 1, dp)
            if p2 != 0:
               for j in range(B-1):
                    ret += (self.countPermutation(r, j, dp) * p2)
            
            ret += (p1 * p2)
            cnt += ret * self.choose(l+r, l)
        
        cnt %= MOD
        dp[(A, B)] = cnt
        return cnt
        
    def choose(self, n, k):
        sm = 1
        for i in range(k):
            sm *= (n-i)
            
        for i in range(2, k+1):
            sm = sm // i
        
        return sm
        
        
