class Solution:
    # @param A : list of integers
    # @return a list of integers
    def prevSmaller(self, A):
        stack = []
        result = []
        for i, a in enumerate(A):
            j = i - 1
            
            if j >= 0 and a > A[j]:
                result.append(a)
                stack.append(A[j])
                continue
            
            k = len(stack) - 1
            
            while k >= 0:
                if a > stack[k]:
                    result.append(stack[k])
                    break
                k -= 1
                
            if k == -1:
                result.append(-1)
            
        return result    
            
            
