class Solution:
    # @param A : list of strings
    # @param B : string
    # @return an integer
    def exist(self, A, B):
        R = len(A)
        if R == 0:
            return 0
            
        C = len(A[0])
        if C == 0:
            return 0
            
        stack = []
        visited = set()
        
        for r in range(R):
            for c in range(C):
                stack.append((B, r, c))
                
        
        while stack:
            w, r, c = stack.pop(-1)
            
            if (w, r, c) in visited:
                continue
            
            if len(w) == 0:
                return 1
                
            if w[0] != A[r][c]:
                continue
            
            visited.add((w, r, c))
            
            rem = w[1:]
            
            if r > 0:
                stack.append((rem, r - 1, c))
                
            if c > 0:
                stack.append((rem, r, c - 1))
                
            if r + 1 < R:
                stack.append((rem, r + 1, c))
                
            if c + 1 < C:
                stack.append((rem, r, c + 1))
        
        
        return 0





