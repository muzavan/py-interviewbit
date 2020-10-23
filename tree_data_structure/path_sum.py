# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    
    def hasPath(self, A, B):
        if not A.left and not A.right:
            return A.val == B
            
        if not A.left:
            return self.hasPath(A.right, B - A.val)
            
        if not A.right:
            return self.hasPath(A.left, B - A.val)
            
        return self.hasPath(A.left, B - A.val) or self.hasPath(A.right, B - A.val)
        
    def hasPathSum(self, A, B):
        return 1 if self.hasPath(A, B) else 0
            
