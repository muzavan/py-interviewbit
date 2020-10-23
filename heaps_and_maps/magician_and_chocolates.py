from heapq import heappush, heappop
class Solution:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def nchoc(self, A, B):
        sm = 0
        l = []
        for a in B:
            heappush(l, -1*a)
            
        for _ in range(A):
            k = -1 * heappop(l)
            # print(k)
            
            sm += k
            sm %= (1e9 + 7)
            
            nx = k // 2
            heappush(l, -1 * nx)
        
        return int(sm)
