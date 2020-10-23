from itertools import permutations
 
def try_merge(s1, s2):
    if s1 in s2:
        return s2, len(s2)
    
    # print("CM:", s1, s2)
    l = len(s2)
    while l > 0:
        ss1 = s1[-l:]
        ss2 = s2[:l]
        if ss1 == ss2:
            break
        l -= 1
        
    return s1 + s2[l:], l
    
def get_key(A):
    return ",".join(A)
    
MAX = 1800
 
class Solution:
    # @param A : list of strings
    # @return an integer
    def solve(self, A):
        As = sorted(A)
        res = self.solveMerge(As, {})
        
        res = sorted(res, key=lambda x : len(x))
        return len(res[0])
        
    def solveMerge(self, A, cache):
        N = len(A)
        
        if N == 1:
            return A
        
        Akey = get_key(A)
        
        if Akey in cache:
            return cache[Akey]
            
        # Search for the most efficient overlapping
        # Score reflecting the maximum overlaping
        score = 0
        candidates = []
 
        for i in range(N):
            s1 = A[i]
            
            for j in range(i+1, N):
                s2 = A[j]
                
                r1, score1 = try_merge(s1, s2)
                r2, score2 = try_merge(s2, s1)
                
                c1 = (i, j, r1, score1)
                c2 = (i, j, r2, score2)
                
                if score1 > score:
                    candidates = [c1]
                    score = score1
                elif score1 == score:
                    candidates.append(c1)
                    
                if score2 > score:
                    candidates = [c2]
                    score = score2
                elif score2 == score:
                    candidates.append(c2)
                    
        
        choiches = ["".join(A)]
        if score != 0:
            choiches = []
            
            for i, j, r, score in candidates:
                new_A = A[:]
                
                # Merge the most efficient overlapping
                del new_A[j]
                del new_A[i]
 
                
                new_A.append(r)
                
                # Seek the path where the most efficient overlapping is applied
                new_A = sorted(new_A)
                nxt = self.solveMerge(new_A, cache)
                choiches = choiches + nxt
        
        cache[Akey] = choiches
        return choiches
