class Solution:
    # @param A : string
    # @return an integer
    ROMAN_MAP = {
        "I" : 1,
        "V" : 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000
    }
    
    ROMAN_CHL = {
        "V" : "I",
        "L" : "X",
        "D" : "C",
        "X" : "I",
        "C" : "X",
        "M" : "C"
    }
    
    def romanToInt(self, A):
        tot = 0
        prev = None
        for a in A:
            tot += self.ROMAN_MAP[a]
            if a in self.ROMAN_CHL and prev == self.ROMAN_CHL[a]:
                tot -= 2 * self.ROMAN_MAP[prev]
            prev = a
            
        return tot
            
            
            
