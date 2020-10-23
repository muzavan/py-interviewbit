MOD = 10**3 + 3

class Solution:
    # @param A : string
    # @return an integer
    def __init__(self):
        self.valid = set(['T', 'F'])
        
    def cnttrue(self, A):
        cache = {}
        t, _ = self.cnt(A, 0, len(A)-1, cache)
        return t
        
    def cnt(self, A, st, en, cache):
        if en < st:
            return 0, 0
        
        if A[st] not in self.valid or A[en] not in self.valid:
            return 0, 0
        
        # Base Case
        if st == en:
            if A[st] == 'T':
                return 1, 0
            if A[st] == 'F':
                return 0, 1
            return 0, 0
        
        if (st, en) in cache:
            return cache[(st, en)]
        
        t, f = 0, 0
        for k in range(st, en):
            leftTrue, leftFalse = self.cnt(A, st, k-1, cache)
            rightTrue, rightFalse = self.cnt(A, k+1, en, cache)
            
            leftTrue %= MOD
            leftFalse %= MOD
            rightTrue %= MOD
            rightFalse %= MOD
            
            op = A[k]
            if op == '|':
                t += ((leftTrue * rightTrue)%MOD) + ((leftTrue * rightFalse)%MOD) + ((leftFalse * rightTrue)%MOD)
                f += (leftFalse * rightFalse) % MOD
            elif op == '&':
                t += (leftTrue * rightTrue) % MOD
                f += ((leftTrue * rightFalse)%MOD) + ((leftFalse * rightTrue)%MOD) + ((leftFalse * rightFalse)%MOD)
            elif op == '^':
                t += ((leftTrue * rightFalse)%MOD) + ((leftFalse * rightTrue)%MOD)
                f += ((leftTrue * rightTrue)%MOD) + ((leftFalse * rightFalse)%MOD)
            
            t %= MOD
            f %= MOD
        
        cache[(st, en)] = t, f
                
        return cache[(st, en)]
            
