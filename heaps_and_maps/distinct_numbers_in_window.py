class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def dNums(self, A, B):
        self.dset = {}
        self.cnt = 0
        if B > len(A):
            return []
            
        for i in range(B):
            self.preApp(None, A[i])
            
        res = []
        res.append(self.cnt)
        
        i = 1
        j = B
        while j < len(A):
            post = A[j]
            pre = A[i-1]
            
            self.preApp(pre, post)
            
            res.append(self.cnt)
            
            i += 1
            j += 1
        
        return res
        
        
    def preApp(self, pre, post):
        if pre is not None:
            self.dset[pre] -= 1
            if self.dset[pre] == 0:
                self.cnt -= 1
                del self.dset[pre]
                
        if post not in self.dset:
            self.cnt += 1
            self.dset[post] = 0
            
        self.dset[post] += 1
            
