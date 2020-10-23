class Solution:
    # @param A : integer
    # @param B : list of integers
    # @param C : list of integers
    # @return an integer
    def solve(self, A, B, C):
        children_map = {}
        
        for b, c in zip(B, C):
            if b not in children_map:
                children_map[b] = []
                
            children_map[b].append(c)
            
        
        for a in range(1, A+1):
            cyclic = self.checkCyclic(a, children_map, set())
            if cyclic:
                return 0
                
                
        return 1

    
    def checkCyclic(self, curr, children_map, visited):
        if curr in visited:
            return True
            
            
        visited.add(curr)
        
        for nxt in children_map[curr]:
            cyclic = self.checkCyclic(nxt, children_map, visited)
            if cyclic:
                return True
        
        visited.remove(curr)
        return False
        
        