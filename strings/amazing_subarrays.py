class Solution:
    # @param A : string
    # @return an integer
    vowels = "aeiouAEIOU"
    def solve(self, A):
        n = 0
        alen = len(A)
        for i in range(alen):
            rem = alen-i
            if A[i] in self.vowels:
                n += rem
                n %= 10003
            
        return n
    
        
