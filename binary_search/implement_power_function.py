class Solution:
    # @param x : integer
    # @param n : integer
    # @param d : integer
    # @return an integer
    cache = {}
    def pow(self, x, n, d):
        if x == 0:
            return 0
        if n == 0:
            return 1
        if n == 1:
            return x % d
            
        key_f = "%d %d %d" % (x,n,d)
        
        if key_f in self.cache:
            return self.cache[key_f]
            
        if n%2 == 0:
            result = (self.pow(x, n/2, d) * self.pow(x, n/2, d)) % d
            self.cache[key_f] = result
            return result
        
        result = (self.pow(x, n/2, d) * self.pow(x, n/2, d) * x) % d 
        self.cache[key_f] = result
        return result
        
