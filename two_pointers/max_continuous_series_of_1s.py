class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of integers
    def maxone(self, A, B):
      zeros = []
      for i, a in enumerate(A):
          if a == 0:
              zeros.append(i)
              
      st = 0
      en = len(A)-1
      
      n = len(zeros)
      
      if n > B:
          mx = 0
          i = 0
          while i < (n - B + 1):
              s = 0 if i == 0 else zeros[i-1]+1
              e = len(A)-1 if (i + B - 1) == (n-1) else zeros[i+B]-1
              
              tmx = (e-s+1)
              #print tmx, s, e
              if tmx > mx:
                  st = s
                  en = e
                  mx = tmx
              
              i += 1
          
      return range(st, en+1)
          

