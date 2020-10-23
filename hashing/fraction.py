class Solution:
    # @param A : integer
    # @param B : integer
    # @return a strings
    def fractionToDecimal(self, A, B):
        minus = False
        if A < 0:
            minus = not minus
            A = -1 * A
        if B < 0:
            minus = not minus
            B = -1 * B
            
        if A == 0:
            return "0"
            
        res = A // B
        m = A % B
            
        pre = "-{}".format(res) if minus else "{}".format(res)
        
        if m != 0:
            pre += "."
        dres = {}
        return self.solve(dres, pre, m*10, B)
        
    def solve(self, dres, pre,  A, B):
        if A == 0:
            return pre
            
        while A != 0:
            if A in dres:
                i = dres[A]
                pre = pre[:i] + "(" + pre[i:] + ")"
                break
            else:
                dres[A] = len(pre)
                
            if A < B:
                A = A*10
                pre += "0"
                continue
                
            r = A // B
            m = A % B
            
            pre += "{}".format(r)
            A = m*10
        
        return pre
        
