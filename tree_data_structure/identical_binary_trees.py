# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        if not A and not B:
            return 1
        elif A and B:
            if A.val != B.val:
                return 0
            else:
                return self.isSameTree(A.left, B.left) and self.isSameTree(A.right, B.right)
        
        return 0
    
            
        
