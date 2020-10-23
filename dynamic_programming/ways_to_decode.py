class Solution:
    # @param A : string
    # @return an integer
    def numDecodings(self, A):
        return self.ways(A)
    
    def ways(self, A):
        ans = 0
        
        if len(A) == 0 or (len(A) == 1 and A[0] != '0'):
            return 1
        
        if self.valid(A[0]):
            ans += self.ways(A[1:])
        if self.valid(A[:2]):
            ans += self.ways(A[2:])
            
        return ans
        
    def valid(self,A):
        return int(A) <= 26 and A[0] != '0'
        
