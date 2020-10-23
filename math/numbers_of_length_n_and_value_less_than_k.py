from collections import Counter

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @param C : integer
    # @return an integer
    def solve(self, A, B, C):
        if len(A) == 0:
            return 0
        
        lenC = len("{0}".format(C))
        if lenC < B:
            return 0
            
        if lenC > B:
            if 0 in A and B != 1:
                return self.permute(len(A), B) - self.permute(len(A), B-1)
            return self.permute(len(A), B)
            
        return self.count_pos(A, C)
        
    def count_pos(self, A, C):
        Cs = "{0}".format(C)
        lenC = len(Cs)
        result = 0
        #print(lenC)
        for i in range(lenC):
            # print("i",i)
            c = int(Cs[i])
            num = 0
            while(num < len(A) and A[num] < c ):
                num += 1
                
            if lenC != 1 and i == 0 and 0 in A:
                num -= 1
            # print("num",num)
            poss = num * self.permute(len(A), lenC-i-1)
            result = result + poss
            
            if c not in A:
                break
            
        return result
        
    def permute(self, lenA, B):
        result = 1
        for _ in range(B):
            result = result * (lenA)
        
        return result

    