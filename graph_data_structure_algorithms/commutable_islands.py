from heapq import heappush, heappop

class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return an integer
    def prim(self, A, B):
        dp = {}
        for i1, i2, b in B:
            if i1 not in dp:
                dp[i1] = {}
            if i2 not in dp:
                dp[i2] = {}
        
            dp[i1][i2] = b
            dp[i2][i1] = b
        
        
        cost = 0
        visited = set()
        
        # Start from island-1, since it's a start, the cost is 0
        # (cost, node)
        pq = [(0, 1)]
        
        while len(pq) > 0:
            c, curr_island = heappop(pq)
            
            if curr_island in visited:
                continue
            
            cost += c
            visited.add(curr_island)
            
            for k, v in dp[curr_island].items():
                heappush(pq, (v, k))
                
        
        return cost
        
    def kruskal(self, A, B):
        Bs = sorted(B, key= lambda x: x[2])
        
        cost = 0
        
        setList = []
        for a, b, c in Bs:
            Aset = -1
            Bset = -1
            
            for i, s in enumerate(setList):
                if a in s:
                    Aset = i
                    
                if b in s:
                    Bset = i
                    
            if Aset == -1 and Bset == -1:
                newSet = set([a, b])
                setList.append(newSet)
                cost += c
                continue
                
            if Aset == Bset:
                # Same set, should ignore this
                continue
            
            if Aset == -1:
                setList[Bset].add(a)
                cost += c
                continue
            
            if Bset == -1:
                setList[Aset].add(b)
                cost += c
                continue
            
            # Found both of them in different set
            # Should merge the set
            
            mnIdx = min(Aset, Bset)
            mxIdx = max(Aset, Bset)
            
            # Pop mxIdx
            # Union it with mnIdx
            mxSet = setList.pop(mxIdx)
            setList[mnIdx] = setList[mnIdx].union(mxSet)
            cost += c
            
            if len(setList) == 1 and len(setList[0]) == A:
                break
        
        return cost
        
    def solve(self, A, B):
        return self.prim(A, B)
        
        
        
