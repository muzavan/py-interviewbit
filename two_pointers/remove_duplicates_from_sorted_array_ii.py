class Solution:
    # @param A : list of integers
    # @return an integer
    def removeDuplicates(self, A):
        na = len(A)
        
        i = 0
        j = 1
        
        if na <= 2:
            return na
            
        prev = A[i]
        alr_same = False
        
        while j < na:
            a = A[j]
            if a != prev:
                i += 1
                A[i] = a
                prev = a
                alr_same = False
            elif not alr_same:
                i += 1
                A[i] = a
                alr_same = True
                
            j += 1
            
        return i + 1
                    
