class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maximumGap(self, A):
        if not len(A):
            return -1
        
        lA = []
        for i in range(len(A)):
            lA.append((A[i], i))
            
        sA = sorted(lA,key=lambda x : x[0])
        
        mA = [a[1] for a in sA]
        mx = mA[-1]
        for i in range(len(mA)-1,-1,-1):
            if mA[i] > mx:
                mx = mA[i]
            else:
                mA[i] = mx
        
        mx = 0        
        for i in range(len(sA)):
            t = mA[i] - i
            if t > mx:
                mx = t
                
        return mx
        