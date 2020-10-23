class Solution:
    # @param A : string
    # @return a list of strings
    LINE_SEP = "{}[],"
    def prettyJSON(self, A):
        res = []
        lvl = 1
        curr = ""
        
        i = 0
        while(i < len(A)):
            a = A[i]
            if a == " ":
                continue
            if a in ['{','[']:
                if curr != "":
                    res.append(self.levelPrint(curr, lvl))
                    curr = ""
                res.append(self.levelPrint(a, lvl))
                lvl += 1
                
            elif a in ['}',']']:
                if curr != "":
                    res.append(self.levelPrint(curr, lvl))
                    curr = ""
                lvl -= 1
                if i != (len(A)-1) and A[i+1] == ',':
                    a = a + ','
                    i += 1
                res.append(self.levelPrint(a, lvl))
                
            elif a == ',':
                curr += a
                res.append(self.levelPrint(curr, lvl))
                curr = ""
            else:
                curr += a
                
                
            i += 1
                
        return res
    
    
    def levelPrint(self, A, n):
        return ((n-1) * "\t") + A
        
    def pushStack(self, S, el):
        S.append(el)
        return S
        
    def peekStack(self, S):
        return S[-1]
        
    def popStack(self, S):
        return (S[:-1], S[-1])
