class Solution:
    # @param A : tuple of strings
    # @return an integer
    GROUPS = {}
    N = 9
    def isValidSudoku(self, A):
        self.initGroups()
        return [1 if self.isValid(A) else 0]

    def checkGroup(self, x, y):
        gx = x / 3
        gy = (y / 3) * 3
        
        return gx + gy
        
    def initGroups(self):
        N = self.N
        g = {}
        for _ in range(N):
            g[_] = []
            
        for i in range(N):
            for j in range(N):
                gr = self.checkGroup(i, j)
                g[gr].append((i, j))
                
        self.GROUPS = g
        
    def isValid(self, B):
        N = 9
        
        # Check Row
        y = 0
        while y < N:
            x = 0
            poss = set()
            for i in range(1, N + 1):
                poss.add(str(i))
                
            while x < N:
                k = B[y][x]
                
                if k != '.':
                    if k in poss:
                        poss.remove(k)
                    else:
                        return False
                x+= 1
            y += 1
            
        # Check Column    
        x = 0
        while x < N:
            y = 0
            poss = set()
            for i in range(1, N + 1):
                poss.add(str(i))
                
            while y < N:
                k = B[y][x]
                if k != '.':
                    if k in poss:
                        poss.remove(k)
                    else:
                        return False
                y+= 1
            x += 1
            
            
        # Check Group
        g = 0
        while g < N:
            poss = set()
            for i in range(1, N + 1):
                poss.add(str(i))
            
            for x, y in self.GROUPS[g]:
                k = B[y][x]
                if k != '.':
                    if k in poss:
                        poss.remove(k)
                    else:
                        return False
            g += 1
            
        return True