class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        As = [a for a in A.split('/') if a != '']
        stack = ['']
        
        for a in As:
            if a == '.':
                continue
            if a == '..' and len(stack) > 1:
                stack.pop(-1)
            else:
                stack.append(a)
        
        return "/".join(stack) if len(stack) > 1 else "/"
            
            
            
        
