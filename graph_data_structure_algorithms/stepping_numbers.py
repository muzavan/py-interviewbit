class Solution:
    # @param A : integer
    # @param B : integer
    # @return a list of integers
    def stepnum(self, A, B):
        visited = set()
        
        queue = [a for a in range(0, 10)]
        
        while queue:
            q = queue.pop()
            
            if q in visited:
                continue
            
            if q > B:
                continue
            
            if q >= A:
                # A <= q <= B
                visited.add(q)
                
            last = q % 10
            
            if last <= 8:
                queue.append(10*q + last + 1)
                
            if last >= 1:
                queue.append(10*q + last - 1)
        
        return sorted([v for v in visited])
