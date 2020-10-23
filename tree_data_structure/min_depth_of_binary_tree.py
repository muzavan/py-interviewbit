# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        if not A:
            return 0
        
        if not A.left and not A.right:
            return 1
        if not A.left:
            return self.minDepth(A.right) + 1
        if not A.right:
            return self.minDepth(A.left) + 1
            
        return min(self.minDepth(A.left), self.minDepth(A.right)) + 1