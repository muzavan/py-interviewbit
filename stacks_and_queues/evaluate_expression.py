class Solution:
    # @param A : list of strings
    # @return an integer
    def evalRPN(self, A):
        ops = '+-/*'
        stk = A
        
        buff = []
        while len(stk) > 0:
            s = stk.pop(0)
            if s not in ops:
                buff.append(int(s))
                continue
            b = buff.pop(-1)
            a = buff.pop(-1)
            
            if s == '+':
                res = a + b
            elif s == '-':
                res = a - b
            elif s == '*':
                res = a * b
            else:
                res = a / b
                
            buff.append(res)
            
        return buff[0]
            
