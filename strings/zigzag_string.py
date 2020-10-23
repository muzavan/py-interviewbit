class Solution:
    # @param A : string
    # @param B : integer
    # @return a strings
    def convert(self, A, B):
        if B == 1:
            return A

        C = []
        for _ in range(B):
            C.append("")
            
        i = 0
        right = False
            
        for a in A:
            C[i] = C[i] + a
            if i == (B-1) or i == 0:
                right = not right
                
            if right:
                i+=1
            else:
                i-=1
            
        
        return "".join(C)
