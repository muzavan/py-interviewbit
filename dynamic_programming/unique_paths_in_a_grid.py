class Solution:
    # @param A : list of list of integers
    # @return an integer
    def uniquePathsWithObstacles(self, A):
        prev = []
        
        R = len(A)
        C = len(A[0])
        
        for r in range(R):
            curr = []
            for c in range(C):
                a = A[r][c]
                
                if a == 1:
                    curr.append(0)
                    continue
                
                # a == 0
                if r == 0 and c == 0:
                    curr.append(1)
                    continue
                
                poss = 0
                if c != 0:
                    poss += curr[-1]
                    
                if r != 0:
                    poss += prev[c]
                    
                curr.append(poss)
            
            prev = curr
        return prev[-1]
        
                
