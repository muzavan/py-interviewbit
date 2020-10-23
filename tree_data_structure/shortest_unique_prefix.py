class Solution:
    # @param A : list of strings
    # @return a list of strings
    def prefix(self, A):
        # Create a map of prefix to its possible string
        preMap = {}
        for a in A:
            l = len(a)
            aList = [a[:i] for i in range(1,l+1)]
            
            for al in aList:
                if al not in preMap:
                    preMap[al] = []
                    
                preMap[al].append(a)
                
        
        minPreMap = {}
        preList = [(k, v) for k, v in preMap.items()]
        preList = filter(lambda a: len(a[1]) == 1, preList)
        
        for k, vs in preList:
            if vs[0] not in minPreMap or len(minPreMap[vs[0]]) > len(k):
                minPreMap[vs[0]] = k
            
        res = [minPreMap[a] for a in A]
        
        return res
            
