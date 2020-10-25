class Solution:
    # @param A : string
    # @param B : string
    # @param C : list of strings
    # @return an integer
    def solve(self, A, B, C):
        # For a faster in check
        C = set(C)
        
        # To make the process uniform
        C.add(A)
        C.add(B)
        
        # Get every possible characters for specific index
        mem = {}
        for c in C:
            for i, w in enumerate(c):
                if i not in mem:
                    mem[i] = set()
                
                mem[i].add(w)
        
        # print(mem)
        visited = set() 
        visited.add(A)
        
        queue = [(A, 1)]
        while queue:
            curr, step = queue.pop(0)
            if curr == B:
                return step
            
            poss = self.get_all_possible_changes(curr, B, mem)
            
            # print(curr, step, poss)
            for p in poss:
                if p in visited:
                    continue
                
                if p not in C:
                    continue
                
                visited.add(p)
                queue.append((p, step+1))
        
        return 0
            
        
    def get_all_possible_changes(self, curr, target, mem):
        # Find the possible modified letter
        # Modification happens 1 by 1
        # Either: to the end string, or other words in the mem
        
        poss = []
        for i, c in enumerate(curr):
            # Already close to the target, skipping
            # if c == target[i]:
            #     continue
            
            # All possibilities
            for ch in mem[i]:
                if ch == c:
                    continue
                p = curr[:i] + ch + curr[i+1:]
                poss.append(p)
        
        return poss
    
    
