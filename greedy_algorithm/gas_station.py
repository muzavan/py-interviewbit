class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        C = [a-b for a, b in zip(A, B)]
        N = len(C)
        
        # Greedy
        # Start with the most surplus
        fuel = 0
        minIdx = 0
        sm = 0
        for i in range(N):
            sm += C[i]
            fuel += C[i]
            
            if fuel < 0:
                fuel = 0
                minIdx = i + 1
                
        if sm >= 0:
            return minIdx % N
        return -1
