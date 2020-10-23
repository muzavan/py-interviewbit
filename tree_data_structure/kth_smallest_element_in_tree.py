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
    def kthsmallest(self, A, B):
        ins = self.inOrder(A)
        return ins[B-1]
    
    def inOrder(self, A):
        if A is None:
            return []
            
        val = A.val
        
        left = self.inOrder(A.left)
        right = self.inOrder(A.right)
        
        return left + [val] + right