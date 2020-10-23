class Solution:
    # @param A : string
    # @return an integer
    def longestValidParentheses(self, A):
        nA = len(A)
        
        i = 0
        longest = []
        while i < nA:
            ai = A[i]
            
            if ai == '(' or i == 0:
                longest.append(0)
            elif ai == ')':
                if A[i-1] == '(':
                    longest.append(longest[i-2]+2)
                else:
                    firstLong = i - longest[i-1]
                    
                    if firstLong > 0 and A[firstLong-1] == '(':
                        lng = longest[i-1]+2
                        
                        if firstLong >= 2:
                            lng += longest[firstLong-2]
                        longest.append(lng)
                    else:
                        longest.append(0)
            
            i += 1
        
        return max(longest)
            
            
                    
        
                
                
        
        
