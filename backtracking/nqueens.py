class Solution:
    # @param A : integer
    # @return a list of list of strings
    DIAGONALS = {}
    def solveNQueens(self, A):
        self.setDiagonals(A)
        qsolved = self.solvingQueens([], A, 0)
        res = []
        
        for q in qsolved:
            res.append(self.formatQueen(q, A))
            
        return res
        
        
    def formatQueen(self, state, N):
        res = []
        y = 0
        while y < N:
            s, _ = state[y]
            board = ('.' * s) + 'Q' + ('.'*(N-s-1))
            res.append(board)
            y += 1
        return res
    
    def solvingQueens(self, pre, A, y):
        ai = A-1
        
        if not self.valid(pre):
            return []
            
        if len(pre) == A:
            return [pre]
        
        res = []
        while ai >= 0:
            pr = pre + [(ai, y)]
            
            tres = self.solvingQueens(pr, A, y+1)
            res.extend(tres)
            
            ai -= 1
        return res
    
    def valid(self, state):
        #print(state)
        for si, s1 in enumerate(state):
            for s2 in state[si+1:]:
                if s1 in self.DIAGONALS[s2]:
                    #print("Not Valid")
                    return False
        
        #print("Valid")
        return True
    
    def setDiagonals(self, N):
        d = {}
        for i in range(N):
            for j in range(N):
                tup = (i, j)
                d[tup] = set()
                
        for i in range(N):
            for j in range(N):
                tup = (i, j)
                d[tup] = self.listMovements(i, j, N)
                
        self.DIAGONALS = d
                
    def listMovements(self, x, y, N):
        res = set()
        # Bottom Right
        i, j = x+1, y+1
        
        while i < N and j < N:
            res.add((i, j))
            i += 1
            j += 1
                
        # Bottom Left
        i, j = x-1, y+1
        
        while i >= 0 and j < N:
            res.add((i, j))
            i -= 1
            j += 1
        
        # Top Right
        i, j = x+1, y-1
        
        while i < N and j >= 0:
            res.add((i, j))
            i += 1
            j -= 1
        
        # Top Left
        i, j = x-1, y-1
        
        while i >= 0 and j >= 0:
            res.add((i, j))
            i -= 1
            j -= 1
            
        # Top
        i, j = x, y-1
        
        while j >= 0:
            res.add((i, j))
            j -= 1
        # Bottom
        i, j = x, y+1
        
        while j < N:
            res.add((i, j))
            j += 1
            
        # Right
        i, j = x+1, y
        while i < N:
            res.add((i, j))
            i += 1
            
        # Left
        i, j = x-1, y
        while i >= 0:
            res.add((i, j))
            i -= 1
            
        return res
                    
            
