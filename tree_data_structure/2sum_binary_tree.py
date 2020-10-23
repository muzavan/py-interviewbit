# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        ins = self.inOrder(A)
        
        s = set()
        for i in ins:
            rem = B - i
            
            if rem in s:
                return 1
            
            s.add(i)    
        return 0
    
    def inOrder(self, A):
        if A is None:
            return []
            
        return self.inOrder(A.left) + [A.val] + self.inOrder(A.right)
