class Solution:
    # @param A : list of list of chars
    # @return nothing
    N = 9
    GROUPS = {}
    ev = []
    def solveSudoku(self, A):
        As = A + []
        self.initGroups()
        
        self.solveSudokuPartial(A, 0, 0, As)
    
    def solveSudokuPartial(self, state, x, y, A):
        N = self.N
        
        if y == N:
            return state
            
        if x + 1 < N:
            nx = x + 1
            ny = y
        else:
            nx = 0
            ny = y + 1
            
        
        if A[y][x] != '.':
            state[y][x] = A[y][x]
            return self.solveSudokuPartial(state, nx, ny, A)
            
        for i in range(1, 10):
            ii = str(i)
            state[y][x] = ii
            
            # self.ev.append((y,x,ii))
            if self.isValid(state):
                res = self.solveSudokuPartial(state, nx, ny, A)
                if res:
                    return res
                
                
        # Backtrack, need to set value back
        state[y][x] = '.'
        return None
    
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
        N = self.N
        
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