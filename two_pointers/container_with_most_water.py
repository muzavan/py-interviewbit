class Solution:
    # @param A : list of integers
    # @return an integer
    def maxArea(self, A):
        i, j = 0, len(A)-1
        mx = 0
        
        while i < j:
            a = A[i]
            b = A[j]
            
            tmx = min(a, b) * (j-i)
            
            if tmx > mx:
                mx = tmx
                
                
            if a > b:
                j -= 1
            else:
                i += 1
            
            
        return mx
        
        
