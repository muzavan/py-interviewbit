# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxDepth(self, A):
        return self.level(A)
    
    def level(self, A):
        if A is None:
            return 0
            
        return max(self.level(A.left), self.level(A.right)) + 1
