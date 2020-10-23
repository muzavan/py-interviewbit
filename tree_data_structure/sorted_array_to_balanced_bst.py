# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : tuple of integers
    # @return the root node in the tree
    def sortedArrayToBST(self, A):
        lA = len(A)
        
        if lA == 0:
            return None
        
        if lA == 1:
            return TreeNode(A[0])
            
        mid = lA/2
        
        tree = TreeNode(A[mid])
        tree.left = self.sortedArrayToBST(A[:mid])
        tree.right = self.sortedArrayToBST(A[mid+1:])
        
        return tree
