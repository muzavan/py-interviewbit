class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        Alist = [c for c in A]
        Alist = sorted(Alist)
        
        # Move through each digits
        befores = 0
        for c in A:
            k = self.findBefore(Alist, c)
            Alist.remove(c)
            befores += k*self.fact(len(Alist))
            befores %= 1000003
            
        
        befores += 1
        befores %= 1000003
        return befores
    
    def findBefore(self, A, a):
        # A is already sorted
        for i in range(len(A)):
            if A[i] == a:
                return i
                
    def fact(self, n):
        tot = 1
        for i in range(1, n+1):
            tot *= i
            
        return tot
    
