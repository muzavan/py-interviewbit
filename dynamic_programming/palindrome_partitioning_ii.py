class Solution:
    # @param A : string
    # @return an integer
    def minCut(self, A):
        dp = {}
        
        return self.cut(A, dp)
        
    def cut(self, A, dp):
        if isPalindrome(A):
            return 0
        
        if A in dp:
            return dp[A]
            
        poss = []
        for i in range(len(A)-1, -1, -1):
            word = A[:i]
            rem = A[i:]
            if isPalindrome(rem):
                poss.append(1 + self.cut(word, dp))
        
        return min(poss)

    
def isPalindrome(A):
    st = 0
    en = len(A) - 1
    
    while en >= st:
        if A[en] != A[st]:
            return False
        st += 1
        en -= 1
        
    return True
