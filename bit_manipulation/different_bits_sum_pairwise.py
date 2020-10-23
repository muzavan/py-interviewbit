class Solution:
    # @param A : list of integers
    # @return an integer
    def cntBits(self, A):
        n = len(A)
        ans = 0
        for i in range(32):
            j = 1<<i
            
            count = 0
            for a in A:
                if a & j:
                    count+=1
                    
            ans += (count * (n-count) * 2)
            
            
        return int(ans % (1e9+7))
