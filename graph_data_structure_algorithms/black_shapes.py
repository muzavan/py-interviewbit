class Solution:
    # @param A : list of strings
    # @return an integer
    def black(self, A):
        R = len(A)
        if R == 0 :
            return 0
            
        C = len(A[0])
        if C == 0:
            return 0
            
        visited = []
        stack = []
        
        for r in range(R):
            currRow = []
            for c in range(C):
                # Row, Column, Flag
                stack.append((r, c, 0))
                currRow.append(0)
                
            visited.append(currRow)
            
        cnt = 0
        
        while len(stack) > 0:
            r, c, flag = stack.pop(-1)
            
            if A[r][c] != 'X':
                continue
            
            if visited[r][c] != 0:
                continue
            
            if flag == 0:
                cnt += 1
                flag = cnt
                
            visited[r][c] = flag
            
            if r > 0:
                stack.append((r-1, c , flag))
                
            if c > 0:
                stack.append((r, c - 1, flag))
                
            if r + 1 < R:
                stack.append((r+1, c, flag))
                
            if c + 1 < C:
                stack.append((r, c+1, flag))
            
        
        return cnt
