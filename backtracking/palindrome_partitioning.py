class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        return self.allPartition(A)
    
    def allPartition(self, A):
        res = []
        
        if len(A) <= 1:
            return A
        
        ai = 0
        
        while ai < len(A):
            pre = A[:ai+1] #String
            alls = self.allPartition(A[ai+1:])
            
            if len(alls) == 0:
                res.append(pre)
            
            for al in alls:
                mn = [pre]
                mn.extend(al)
                res.append(mn)
            ai += 1
            
        return res
        
    def isPalindrom(self, A):
        i = 0
        j = len(A)-1
        
        while i < j:
            if A[i] != A[j]:
                return False
            i += 1
            j -= 1
            
        return True
        
