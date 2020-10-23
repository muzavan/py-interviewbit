class Solution:
    # @param A : string
    # @return an integer
    INT_MAX = 2147483647
    INT_MIN = 2147483648
    
    INTS = '0123456789'
    
    def atoi(self, A):
        MAPS = {a:i for i,a in enumerate(self.INTS)}
        i = 0
        pos = True
        if A[i] == '-' or A[i] == '+':
            pos = A[i] == '+'
            A = A[1:]
            
        num = []
        for i in range(len(A)):
            if A[i] in self.INTS:
                num.append(MAPS[A[i]])
                continue
            break
        
        tot = 0
        i = len(num)-1
        
        bas = 1
        while i >= 0:
            tot += (num[i] * bas)
            bas *= 10
            i -= 1
            
        if pos and tot > self.INT_MAX:
            tot = self.INT_MAX
            
        if not pos and tot > self.INT_MIN:
            tot = self.INT_MIN
            
        return tot if pos else -1*tot
        
        
