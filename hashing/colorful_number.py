class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        lt = [int(a) for a in "{}".format(A)]
        
        s = set()
        k = 1
        while k <= len(lt):
            for i in range(0, len(lt)-k+1):
                # print(lt[i:i+k])
                xx = 1
                for x in lt[i:i+k]:
                    xx *= x
                   
                if xx in s:
                    return 0
                s.add(xx)
                
            k += 1
        return 1            


            
            