class Solution:
    # @param A : list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        # Calculate expected sum
        B = [a for a in A if a > 0]
        B = sorted(B)
        for i,b in enumerate(B):
            if b != i+1:
                return i+1
                
        return len(B) + 1
        
        
        
