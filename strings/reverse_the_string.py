class Solution:
    # @param A : string
    # @return string
    def reverseWords(self, A):
        A = A.strip()
        B = A.split()
        B.reverse()
        
        return " ".join(B)