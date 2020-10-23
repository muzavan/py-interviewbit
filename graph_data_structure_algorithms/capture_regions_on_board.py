class Solution:
    # @param A : list of list of chars
    def solve(self, A):
        return solve(A)
    
def solve(A):
    R = len(A)
    if R == 0:
        return A
        
    C = len(A[0])
    if C == 0:
        return A
        
    # Idea, we iterate from 'O' in the outer layer
    
    visited = set()
    
    queue = []
    
    for r in range(R):
        for c in range(C):
            if r == 0 or c == 0 or r == R - 1 or c == C - 1:
                a = A[r][c]
                
                if a == 'O':
                    queue.append((r, c))
                continue
            
    while queue:
        r, c = queue.pop(0)
        
        if (r, c) in visited:
            continue
        
        a = A[r][c]
        
        if a == 'X':
            continue
        
        visited.add((r, c))
        
        if r > 0:
            queue.append((r-1, c))
            
        if c > 0:
            queue.append((r, c-1))
            
        if r < R - 1:
            queue.append((r+1, c))
            
        if c < C - 1:
            queue.append((r, c+1))
            
        
    # All not in visited will be turned as X
    
    for r in range(R):
        for c in range(C):
            a = A[r][c]
            
            if a != 'O':
                continue
            
            if (r, c) in visited:
                continue
            
            A[r][c] = 'X'
        
    return A
