class Solution:
    # @param A : string
    # @return an integer
    def power(self, A):
        a = int(A)
        m = 0
        while (m == 0 and a > 2):
            try:
                m = m + (a % 2)
                a = int(a//2)
            except:
                m = 1
            
        return 1 if (a == 2 and m == 0) else 0
