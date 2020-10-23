# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        if A is None:
            return None
        curr = A
        left = curr.left
        curr.left = self.invertTree(curr.right)
        curr.right = self.invertTree(left)
        return curr
    
        
        
