class Solution:
    # @param A : string
    # @return a list of strings
    TTC = {
        "0": "0",
        "1": "1",
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    def letterCombinations(self, A):
        A = str(A)
        
        return self.allCombination("", A)
    
    def allCombination(self, pre, A):
        if len(A) == 1:
            return ["{}{}".format(pre, a) for a in self.TTC[A[0]]]
            
        res = []
        for a in self.TTC[A[0]]:
            npre = "{}{}".format(pre, a)
            tres = self.allCombination(npre, A[1:])
            res.extend(tres)
            
        return res
