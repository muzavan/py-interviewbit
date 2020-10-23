class Solution:
    # @param A : string
    # @param B : list of strings
    # @return an integer
    def wordBreak(self, A, B):
        dp = {}
        B = set(B)
        return 1 if self.word(A, B, dp) else 0
        
    def word(self, A, B, dp):
        if len(A) == 0:
            return True
            
        if A in dp:
            return dp[A]
            
        for i in range(len(A)):
            remWord = A[i:]
            if len(remWord) == 0:
                continue
            
            if remWord in B:
                if self.word(A[:i], B, dp):
                    dp[A] = True
                    return True
                    
        dp[A] = False
        return False
            
            
