class Solution:
    # @param A : list of integers
    # @return an integer
    def canJump(self, A):
        mx = 0
        curr = 0
        visited = set()
        
        while mx < len(A) - 1 and len(visited) != len(A) and curr >= 0:
            if curr not in visited:
                mx = max(mx, curr + A[curr])
                visited.add(curr)
                curr = curr + A[curr]
            else:
                curr -= 1
        
        return 1 if mx >= len(A)-1 else 0
