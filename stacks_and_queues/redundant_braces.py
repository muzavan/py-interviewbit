class Solution:
    # @param A : string
    # @return an integer
    def braces(self, A):
        stack = []
        ai = 0
        
        while ai < len(A):
            a = A[ai]
            # print(a, stack)
            if a == ')':
                char = stack.pop(-1)
                containEx = False
                
                while char != '(':
                    if char in ['+','-','*','/']:
                        containEx = True
                    char = stack.pop(-1)
                    
                # print(stack, containEx)
                
                stack.append('a')
                if not containEx:
                    return 1
                
            else:
                stack.append(a)
                
            ai += 1
            
        return 0
