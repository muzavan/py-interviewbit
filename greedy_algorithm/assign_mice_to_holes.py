class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def mice(self, A, B):
        A = sorted(A)
        B = sorted(B)
        
        return max([abs(a - b) for a, b in zip(A, B)])
