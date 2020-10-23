class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        # Change B to set to make the search faster
        B = set(B)
        return self.breakTheWord(A, B, {})
        
    def breakTheWord(self, A, B, dp):
        # dp store the possible sentences form up to idx
        invB = {}
        
        for b in B:
            k = b[-1]
            
            if k not in invB:
                invB[k] = []
                
            invB[k].append(b)
        
        for idx, a in enumerate(A):
            poss = []
            if a in invB:
                poss = invB[a]
            
            els = []    
            for p in poss:
                lp = len(p)
                
                st = idx+1 - lp
                en = idx+1
                
                if st >= 0 and A[st:en] == p:
                    if st == 0:
                        els.append(p)
                    else:
                        for d in dp[st-1]:
                            els.append(d + " " + p)
                            
            
            dp[idx] = els
            
        # from pprint import pprint
        # pprint(dp)
        
        return sorted(dp[len(A)-1]) if len(dp[len(A)-1]) > 0 else []
            
        