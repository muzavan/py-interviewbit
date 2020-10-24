class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @param F : integer
    # @return an integer
    def knight(self, A, B, C, D, E, F):
        # Note: based on problem description: C, D, E, F is 1-based index
        # Using BFS, so a particular cell probably will be first visited
        # on the minimum step (can think step as the level of traversal)
        
        # (X, Y) -> minstep
        visited = []
        
        for _ in range(A):
            visited.append([False] * B)
        
        queue = [(C, D, 0)]
        self.setmx(visited, C, D, True)
        while queue:
            c, d, step = queue.pop(0)
            if c == E and d == F:
                return step
            
            nxts = self.generate_next_move(A, B, c, d, step)
            for n in nxts:
                if self.getmx(visited, n[0], n[1]):
                    continue
                
                self.setmx(visited, n[0], n[1], True)
                queue.append(n)
        
        return -1
        
        
    def generate_next_move(self, A, B, c, d, step):
        nxt = step + 1
        moveset = [
            (-2, -1),
            (-1, -2),
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1)  
        ]
        
        lst = []
        for mv in moveset:
            ct, dt = mv
            nc, nd = (c + ct, d + dt)
            
            if nc < 1 or nc > A or nd < 1 or nd > B:
                # out of bound
                continue
            
            lst.append((nc, nd, nxt))
        
        return lst
        
    def setmx(self, mx, a, b, val):
        mx[a-1][b-1] = val
        
    def getmx(self, mx, a, b):
        return mx[a-1][b-1]
        
