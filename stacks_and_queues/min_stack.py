class MinStack:
    
    def __init__(self):
        self.stk = []
        self.qs = []
    
    # @param x, an integer
    def push(self, x):
        self.stk.append(x)
        
        if len(self.qs) == 0:
            self.qs.append(x)
        elif x < self.qs[0]:
            self.qs = [x] + self.qs
        return x
            

    # @return nothing
    def pop(self):
        if len(self.stk) > 0:
            x = self.stk.pop(-1)
            k = 0
            while k < len(self.qs):
                if x == self.qs[k]:
                    self.qs.pop(k)
                    break
                k += 1
        
        return

    # @return an integer
    def top(self):
        return self.stk[-1] if len(self.stk) > 0 else -1


    # @return an integer
    def getMin(self):
        return self.qs[0] if len(self.qs) > 0 else -1

