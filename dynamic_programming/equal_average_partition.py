class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    A = None
    def avgset(self, A):
        self.A = sorted(A)
        return self.find(A)
    
    
    def find(self, A):
        self.A = sorted(A)
        s = sum(A)
        ls = len(A)
        
        # The average is same if 
        # (s - sum(s1)) * len(s1) = (len(s) - len(s1)) * sum(s1)
        # s * len(s1) = len(s) * sum(s1)
        # sum(s1) = s * l1 / ls
        
        a1 = None
        dp = {}
        for l1 in range(1, ls):
            s1 = s * l1
            a1 = self.findS1(ls, l1, s1, 0, dp)
            
            if a1 is not None:
                break
        
        if a1 is None:
            return []
    
        a2 = split(a1, A)
        return a1, a2
    
    def findS1(self, ls, l, target, idx, dp):
        if target == 0 and l == 0:
            return []
            
        if target == 0 or l == 0 or len(self.A) == idx:
            return None
            
        key = (l, target, idx)
        
        if key in dp:
            return dp[key][0]
            
        # See if we can put A[0]
        p1 = [self.A[idx]]
        xx = self.findS1(ls, l - 1, target - (self.A[idx]*ls), idx+1, dp)
        if xx is None:
            p1 = None
        else:
            p1 = p1 + xx

        # or Not
        p2 = self.findS1(ls, l, target, idx+1, dp)
        
        if p1 is None and p2 is None:
            dp[key] = (None, True)
            return None
            
        if p1 is None:
            dp[key] = (p2, True)
            return p2
            
        if p2 is None:
            dp[key] = (p1, True)
            return p1
            
        if len(p1) <= len(p2):
            dp[key] = (p1, True)
            return p1
            
        dp[key] = (p2, True)
        return p2
        
            
def split(s1, A):
    s2 = A[:]
    
    for s in s1:
        s2.remove(s)
        
    return s2
    
        
