class Solution:
    # @param A : integer
    # @return an integer
    def reverse(self, A):
        if A < 0:
            return int("-{0}".format(self.reverse(-1*A)))
        Astr = "{0}".format(A)
        Al = [c for c in Astr]
        Al.reverse()
        Astr = "".join(Al)
        
        if int(Astr) > (1<<31):
            return 0
            
        return int(Astr)
