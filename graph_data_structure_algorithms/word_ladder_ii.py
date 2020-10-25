class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return a list of list of strings
    def findLadders(self, start, end, dictV):
        dictV = set(dictV)
        dictV.add(end)
        
        mem = {}
        
        for i in range(len(start)):
            mem[i] = set()
            for w in dictV:
                mem[i].add(w[i])
        
        visited = set()        
        queue = [[start]]
        
        limit = len(dictV) + 1
        
        res = []
        while queue:
            q = queue.pop(0)
            
            if q[-1] == end:
                if len(q) < limit:
                    limit = len(q)
                    res = [q]
                elif len(q) == limit:
                    res.append(q)
                    
                continue
                
            poss = self.get_poss(q[-1], mem)
            
            for po in poss:
                p = q + [po]
                # There is a duplicate element!
                if len(p) != len(set(p)):
                    continue
                
                if tuple(p) in visited:
                    continue
                
                if p[-1] not in dictV:
                    continue
                
                if len(p) > limit:
                    continue
                
                visited.add(tuple(p))
                queue.append(p)
                
        
        
        return res
        
    def get_poss(self, curr, mem):
        poss = []
        
        for i, c in enumerate(curr):
            for ch in mem[i]:
                nxt = curr[:i] + ch + curr[i+1:]
                poss.append(nxt)
                
        return poss
