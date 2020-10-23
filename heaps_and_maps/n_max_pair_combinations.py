from heapq import heappush, heappop

class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of integers
    def solve(self, A, B):
        N = len(A)
        As = sorted(A)
        Bs = sorted(B)
        
        flag = set()
        res = []
        hp = []
        
        s = -1*(As[N-1]+Bs[N-1])
        val = (s, (N-1, N-1))
        
        heappush(hp, val)
        for _ in range(N):
            tmp = heappop(hp)
            res.append(-1*tmp[0])
            
            i, j = tmp[1]
            
            s = -1*(As[i-1] + Bs[j])
            
            if (i-1, j) not in flag:
                flag.add((i-1, j))
                heappush(hp, (s, (i-1, j)))
                
            s = -1*(As[i] + Bs[j-1])
            if (i, j-1) not in flag:
                flag.add((i, j-1))
                heappush(hp, (s, (i, j-1)))
            
            
        return res

        
        
