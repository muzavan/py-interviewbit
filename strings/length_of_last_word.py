class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLastWord(self, A):
        length = 0
        space = True
        for a in A:
            if a == ' ':
                space = True
                
            elif space == True:
                length = 1
                space = False
            else:
                length += 1
                
                
        return length
        
