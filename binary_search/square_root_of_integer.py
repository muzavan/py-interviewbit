class Solution:
    # @param A : integer
    # @return an integer
    def sqrt(self, A):
        l = self.order(A)
        u = 10*l
        
        while(l < u):
            m = (l + u) / 2
            
            # print(l, m , u)
            if m == l:
                break
            
            mm = m * m
            if A == mm:
                l = m
                break
            
            if A < mm:
                u = m
                
            if A > mm:
                l = m
                
        
        return l
            
    
    def order(self, A):
        l = 1
        while(A >= l*l):
            l *= 10
            
        return l/10
