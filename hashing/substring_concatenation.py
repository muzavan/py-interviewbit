class Solution:
    # @param A : string
    # @param B : tuple of strings
    # @return a list of integers
    def findSubstring(self, A, B):
        nB = len(B)
        nL = len(B[0])
        res = []
        
        if nL*nB <= len(A):
            # generate all possible
            poss = self.generate("", B)
           
            for i in range(0,len(A)):
                s = A[i:i+(nL*nB)]
                # print(s)
                if s in poss:
                    res.append(i)
        
        return res
        
    
    
    def generate(self, pre, B):
        B = list(B)
        
        res = set()
        
        if len(B) == 1:
            res.add(pre+B[0])
            return res
            
        for i, b in enumerate(B):
            nl = self.generate(pre + b, B[:i]+B[i+1:])
            for n in nl:
                res.add(n)
        
        return res
