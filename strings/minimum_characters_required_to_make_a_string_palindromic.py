class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        # idea is, find possible mid
        # then count the necessary character count to be inserted
        if len(A) ==  1:
            return 0
            
        
        mid = len(A) // 2
        
        A = list(A)
        for m in range(mid,-1,-1):
            addition = self.odd_palindrom(A, m)
            addition = self.even_palindrom(A, m) if addition == -1 else addition
            
            if addition != -1:
                break
            
        if addition == -1:
            addition = len(A)-1
            
        return addition
    
    def odd_palindrom(self, A, mid):
        # odd case
        rights = A[(mid+1):]
        lefts = A[:mid]
        
        if len(lefts) > len (rights):
            return -1
        
        lefts.reverse()
        same = False
        for l,r in zip(lefts, rights):
            if l == r:
                same = True
                continue
                
            same = False
            break
        
        print(same)
        return (len(rights) - len (lefts)) if same else -1
        
    def even_palindrom(self, A, mid):
        # odd case
        rights = A[mid:]
        lefts = A[:mid]
        
        if len(lefts) > len (rights):
            return -1
        
        lefts.reverse()
        same = False
        for l,r in zip(lefts, rights):
            if l == r:
                same = True
                continue
                
            same = False
            break
        
        print(same)
        
        return (len(rights) - len (lefts)) if same else -1
        
