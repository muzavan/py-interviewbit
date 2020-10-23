class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        d = {}
        ks = []
        for i, a in enumerate(A):
            k = "".join(sorted(a))
            
            if k not in d:
                ks.append(k)
                d[k] = []
                
            d[k].append(i+1)
            
        res = [d[k] for k in ks]
        
        return res