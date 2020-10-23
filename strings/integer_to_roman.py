class Solution:
    # @param A : string
    # @return an integer
    ROMAN_MAP = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")]
    
    def intToRoman(self, A):
        tot = A
        if tot < 1 or tot > 3999:
            return ""
        
        res = []
        for n, s in self.ROMAN_MAP:
            while(tot >= n):
                res.append(s)
                tot -= n
            
        return "".join(res)
            
            
            
