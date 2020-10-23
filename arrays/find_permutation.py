class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        mn = 1
        mx = B
        R = []
        for a in A:
            if a == "I":
                b = mn
                mn += 1
            else:
                b = mx
                mx -= 1
                
            R.append(b)
        
        R.append(mn)
        return R