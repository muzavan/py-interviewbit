class Solution:
    # @param A : list of integers
    # Modify the array A which is passed by reference. 
    # You do not need to return anything in this case. 
    def arrange(self, A):
        N = len(A)
        for i, a in enumerate(A):
            old_value = A[i]
            new_value = A[a] if a > i else (A[a] % N)
            
            A[i] = old_value + new_value * N
            
        for i, a in enumerate(A):
            A[i] = a/N
            
        