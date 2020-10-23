class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def solve(self, A, B):
        dp = {}
        return self.lcs(A, B, dp)
        
        
    def lcs(self, A, B, dp):
        if len(A) == 0 or len(B) == 0:
            return 0
            
        if (A, B) in dp:
            return dp[(A, B)]
            
        res = 0
        
        for ai, a in enumerate(A):
            remA = A[:ai]
            for bi, b in enumerate(B):
                remB = B[:bi]
                
                prev = self.lcs(remA, remB, dp)
                
                if a == b:
                    prev += 1
                    
                res = max(res, prev)
        
        dp[(A, B)] = res
        dp[(B, A)] = res
        return res
