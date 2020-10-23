class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def multiply(self, A, B):
        B = B[::-1]
        tot = "0"
        for i, b in enumerate(B):
            s = self.multiplyDigit(A, b) + ("0" * i)
            tot = self.plus(s, tot)
        
        while (len(tot) > 1 and tot[0] == '0'):
            tot = tot[1:]
            
        return tot
    
    def multiplyDigit(self, A, b):
        A = A[::-1]
        b = int(b)
        carr = 0
        C = []
        
        for a in A:
            n = int(a)
            s = n * b + carr
            C.append(s%10)
            carr = s//10
            
        if carr > 0:
            C.append(carr)
            
        return "".join([str(c) for c in C[::-1]])
    
    def plus(self, A, B):
        if len(B) > len(A):
            return self.plus(B, A)
            
        B = ("0" * (len(A) - len(B))) + B
        A = A[::-1]
        B = B[::-1]
        
        C = []
        
        carr = 0
        for a, b in zip(A, B):
            s = int(a) + int(b) + carr
            C.append(s%10)
            carr = s//10
            
        if carr > 0:
            C.append(carr)
            
        return "".join([str(c) for c in C[::-1]])
            
