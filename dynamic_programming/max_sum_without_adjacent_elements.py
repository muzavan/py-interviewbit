class Solution:
    # @param A : list of list of integers
    # @return an integer
    def adjacent(self, A):
        dp = {}
        
        return self.sum_adjacent(A, dp)
        
        
    def sum_adjacent(self, A, dp):
        mA = [max(A[0][idx], A[1][idx]) for idx in range(len(A[0]))]
        
        dp = {}
        
        for i in range(len(mA)):
            # Whether we choose this element or not
            if i == 0:
                dp[(i, True)] = mA[i]
                dp[(i, False)] = 0
                continue
            
            dp[(i, True)] = mA[i] + dp[(i-1, False)]
            dp[(i, False)] = max(dp[(i-1, True)], dp[(i-1, False)])
        
        return max([v for k, v in dp.items()])
        
