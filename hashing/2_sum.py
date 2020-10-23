class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return a list of integers
    def twoSum(self, A, B):
        # 5 3 3 2 1
        # 5
        # diff = B - a
        # Set 
        # Map -> Element sbg Key -> Index -> Value 
        pastMap = {}
        
        for i, a in enumerate(A):
            diff = B - a
            
            if diff in pastMap:
                return [pastMap[diff], i + 1]
        
            if a not in pastMap:
                pastMap[a] = i + 1
            
        return []
        
        
        
