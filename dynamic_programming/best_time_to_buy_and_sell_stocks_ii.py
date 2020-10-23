class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxProfit(self, A):        
        profits = 0
        prev = 0
        for idx, curr in enumerate(A):
            if idx != 0:
                if curr > prev:
                    profits += (curr - prev)
            
            prev = curr
        
        
        return profits
