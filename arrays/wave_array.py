class Solution:
# @param A : list of integers
# @return a list of integers
    def wave(self, A):
        A = sorted(A)
        A1 = [a for i,a in enumerate(A) if i%2 == 1]
        A2 = [a for i,a in enumerate(A) if i%2 == 0]

        Am = []
        a = None
        
        if len(A2) > len(A1):
            a = A2.pop()

        for a1,a2 in zip(A1,A2):
            Am.append(a1)
            Am.append(a2)

        if a:
            Am.append(a)

        return Am