class Solution:
    # @param A : string
    # @return an integer
    VALID_CHARS = '0123456789-.e+'
    BASE_NUM = '0123456789'
    def isNumber(self, A):
        A = A.strip()
        if len(A) == 0:
            return 0
            
        
        for a in A:
            if a not in self.VALID_CHARS:
                return 0

        if self.isBasicNumeric(A):
            return 1
            
        B = A.split('e')
        
        if len(B) == 2:
            return self.isBasicNumeric(B[0]) * self.isValidNeg(B[1])
            
        return 0
    
    def isInteger(self, A):
        if len(A) == 0:
            return 0
            
        for a in A:
            if a not in self.BASE_NUM:
                return 0
                
        return 1
        
    def isBasicNumeric(self, A):
        B = A.split('.')
        
        if len(B) > 2 or len(B) == 0:
            return 0
        if len(B) == 2:
            B[0] = '0' if B[0] == '' else B[0]
            B[1] = 'xx' if B[1] == '' else B[1]
            return self.isValidNeg(B[0]) * self.isInteger(B[1])
            
        return self.isValidNeg(A)
        
    def isValidNeg(self, A):
        if A[0] == '-' or A[0] == '+':
            return self.isInteger(A[1:])
            
        return self.isInteger(A)
