class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        a_list = A.split(".")
        b_list = B.split(".")
        
        for a, b in zip(a_list, b_list):
            ai = int(a)
            bi = int(b)
            
            if ai == bi:
                continue
            if ai > bi:
                return 1
            return -1
            
        if len(a_list) > len(b_list):
            a_list, b_list = b_list, a_list
            
            
        i = len(a_list)
        while i < len(b_list):
            bi = int(b_list[i])
            if bi == 0:
                i += 1
                continue
            return 1
                
        return 0
