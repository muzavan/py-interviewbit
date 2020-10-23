class Solution:
    # @param A : integer
    # @return an integer
    def isPalindrome(self, A):
        Astr = "{}".format(A)
        Bstr = "{}".format(A)
        B = [c for c in Bstr]
        B.reverse()
        Bstr = "".join([c for c in B])
        return Astr == Bstr
