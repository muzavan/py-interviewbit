class Solution:
    # @param A : integer
    # @return a strings
    def countAndSay(self, A):
        if A < 1:
            return ""
        return self.countAndSayIteration("1", A-1)
    
    def countAndSayIteration(self, As, n):
        if n == 0:
            return As
            
        a_len = len(As)
        a_i = 0
        
        next_str = []
        while a_i < a_len:
            curr_num = As[a_i]
            recur = 0
            while ( a_i < a_len and As[a_i] ==  curr_num):
                recur += 1
                a_i += 1
                
            next_str.append("%d" % recur)
            next_str.append(curr_num)
            
        next_str = "".join(next_str)
        
        return self.countAndSayIteration(next_str, n - 1)
            
