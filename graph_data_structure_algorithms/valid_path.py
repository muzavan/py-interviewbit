class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : list of integers
    # @param F : list of integers
    # @return a strings
    def solve(self, A, B, C, D, E, F):
        x, y = A, B
        _, R = C, D
        
        funcs = []
        for e, f in zip(E, F):
            fun = generateFunc(e, f, R)
            funcs.append(fun)
                    
        visited = set()
        queue = [(0, 0)]
        
        # printRad(funcs, x, y)
        # return "NO"
        
        while len(queue) > 0:
            q = queue.pop(0)
            if q in visited:
                continue
            
            visited.add(q)
            if q == (x, y):
                return "YES"
            
            additional = [g for g in generate(q[0], q[1], x, y) if g not in visited and not red(funcs, *g)]
            queue.extend(additional)
        
        return "NO"
 
 
def printRad(fs, x, y):
    alls = []
    
    for i in range(x+1):
        bs = []
        for j in range(y+1):
            k = red(fs, i, j)
            
            if k:
                bs.append("#")
            else:
                bs.append(" ")
                
        alls.append("".join(bs))
    
    print("\n".join(alls))

def red(fs, a, b):
    for f in fs:
        if f(a, b):
            return True
            
    return False
    
def generate(a, b, x, y):
    k = list()
    for i in range(a-1, a+1+1):
        if i < 0 or i > x:
            continue
        for j in range(b-1, b+1+1):
            if j < 0 or j > y:
                continue
            
            if i == a and j == b:
                continue
            k.append((i, j))
            
    return k
            

def generateFunc(xp, yp, r):
    def f(x, y):
        res = (x - xp) * (x - xp) + (y - yp) * (y - yp)
        return res <= (r * r) 
        
    return f
