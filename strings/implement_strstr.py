class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def strStr(self, B, A):
        M = len(A)
        N = len(B)
        
        if M > N:
            return -1
            
        i, j = 0, 0
        lps = self.lps(A)
        
        while i < N:
            if A[j] == B[i]:
                j += 1
                i += 1
                
            if j == M:
                return i-j
                
            elif i < N and A[j] != B[i]:
                if j > 0:
                    j = lps[j-1]
                else:
                    i += 1
            
        return -1

    def lps(self, _string):
        result = []
        for idx in range(len(_string)):
            subp = _string[:idx+1]
            result.append(self.get_lps(subp))
            
        return result
        
    def get_prefixes(self,subp):
        res = [""]
        for i in range(len(subp)):
            res.append(subp[:i])
            
        return res
        
    def get_suffixes(self,subp):
        res = [""]
        for i in range(len(subp)-1, -1, -1):
            res.append(subp[i:])
            
        return res
        
    def get_lps(self, S):
        prefixes = set(self.get_prefixes(S))
        suffixes = set(self.get_suffixes(S))
        
        best = 0
        for p in prefixes:
            if p in suffixes:
                if len(p) > best:
                    best = len(p)
                    
        return best
