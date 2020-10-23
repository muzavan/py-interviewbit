# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : list of integers
    # @return the root node in the tree
    def buildTree(self, A):
        if A is None or len(A) == 0:
            return None
            
        r = max(A)
        i = 0
        for i, v in enumerate(A):
            if v == r:
                break
            pass
        
        tree = TreeNode(r)
        
        tree.left = self.buildTree(A[:i])
        tree.right = self.buildTree(A[i+1:])
        
        return tree
