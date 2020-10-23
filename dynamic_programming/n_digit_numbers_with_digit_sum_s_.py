MOD = 10**9 + 7

from collections import defaultdict
from pprint import pprint

class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        
        if (B == 0):
            return 0

        def findCombos(n, target):
            first = []
            second = [0 for x in range(target + 1)]
            total = 0
            
            for j in range (1, n + 1):
                for k in range(target + 1):
                    if (k == 0):
                        second[k] = 0
                    elif (j == 1):
                        if k > j * 9:
                            second[k] = 0
                        else:
                            second[k] = 1
                    else:
                        if k < 10:
                            total = total + first[k]
                        else:
                            total = total + first[k] - first[k - 10]
                        
                        if k > j * 9:
                            second[k] = 0
                        else:
                            second[k] = total
            
                first = second
                second = [1 for x in range(target + 1)]
                total = 0

            return first[B] % 1000000007
            
        return findCombos(A, B)
        
