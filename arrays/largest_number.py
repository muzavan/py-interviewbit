class Solution:
    # @param A : tuple of integers
    # @return a strings
    def compare(self, a, b):
        if "{0}{1}".format(a,b) < "{0}{1}".format(b,a):
            return -1
        return 1
        
    def largestNumber(self, A):
        As = ["{0}".format(a) for a in A]
        res = sorted(As, cmp=self.compare, reverse=True)
        res = "".join(res)
        
        all_z = sum([1 for r in res if r=="0"]) == len(res)
        return res if not all_z else "0"