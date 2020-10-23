class Solution:
    # @param A : integer
    # @return an integer
    def trailingZeroes(self, A):
        five = 5
        zero = 0
        while(A//five) != 0:
            res = A // five
            zero += res
            five *= 5
        return zero
