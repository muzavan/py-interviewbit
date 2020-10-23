class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def maxPoints(self, A, B):
        
        mx  = 0
        
        for i in range(len(A)):
            x1, y1 = A[i], B[i]
            slope = {}
            same = 1
            for j in range(i+1, len(A)):
                x2, y2 = A[j], B[j]
                
                if x1 == x2 and y1 == y2:
                    same += 1
                    
                else:
                    m = float('inf')
                    if x1 != x2:
                        m = ((y1-y2) * 1.0) / (x1-x2)
                        
                    if m not in slope:
                        slope[m] = 0
                    slope[m] += 1
            
            
            curr_max = same
            for m in slope:
                curr_max = slope[m] + same if (slope[m] + same) > curr_max else curr_max
                
                
            mx = max(curr_max, mx)
        
        return mx
                
                
