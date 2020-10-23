class Solution:
    # @param A : string
    # @return an integer
    ALPHABETS = "abcdefghijklmnopqrstuvwxyz0123456789"
    def isPalindrome(self, A):
        A_ = A.lower()
        A_ = [x for x in A_ if x in self.ALPHABETS]
        cnt = len(A_)
        
        scnt = 0
        ecnt = cnt-1
        
        while scnt <= ecnt:
            if not A_[scnt] == A_[ecnt]:
                return 0
            scnt += 1
            ecnt -= 1
            
        return 1
