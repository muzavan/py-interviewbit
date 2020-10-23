class Solution:
    # @param A : string
    # @param B : string
    # @return a strings
    def addBinary(self, A, B):
        if len(A) < len(B):
            return self.addBinary(B, A)
            
        # A  >= B
        added = len(A) - len(B)
        B = ("0" * added) + B
        
        A = [a for a in A[::-1]]
        B = [b for b in B[::-1]]
        
        carry = False
        c = []
        for a, b in zip(A, B):
            if a == '1' and b == '1':
                if carry:
                    c.append('1')
                else:
                    c.append('0')
                
                carry = True
                    
            elif a == '0' and b == '0':
                if carry:
                    c.append('1')
                else:
                    c.append('0')
                    
                carry = False
                
            else:
                if carry:
                    c.append('0')
                else:
                    c.append('1')
                    
        if carry:
            c.append('1')
        
        return "".join(c[::-1])
