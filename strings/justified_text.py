class Solution:
    # @param A : list of strings
    # @param B : integer
    # @return a list of strings
    def fullJustify(self, A, B):
        k = 0
        C = []
        tmp = []
        for i in range(len(A)):
            if (k+len(A[i])) <= B:
                k += len(A[i])
                k += 1
                tmp.append(A[i])
                
            else:
                C.append(self._format(tmp, B))
                k = len(A[i])
                tmp = [A[i]]
                k += 1
                
        if len(tmp) > 0:
            C.append(self._lastline(tmp, B))
        
        return C
    
    def _format(self, A, n):
        if len(A) == 1:
            return self._lastline(A,n)
        spaces = len(A) - 1
        n -= (sum([len(a) for a in A]))
        sp = [n//spaces] * spaces
        for i in range(n%spaces):
            sp[i] = sp[i] + 1
            
        res = ""
        for i in range(spaces):
            res += A[i]
            res += (" "*sp[i])
        
        res += A[-1]
        return res
        
    def _lastline(self, A, n):
        n -= (sum([len(a) for a in A]) + len(A) - 1)
        return " ".join(A) + (" " * n)
