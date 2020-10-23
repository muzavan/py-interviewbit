# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
 
class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return the root node in the tree
    def buildTree(self, A, B):
        if len(A) == 0:
            return None
            
        root = TreeNode(A[0])
        rootIdx = B.index(A[0])
        
        inLeft = B[:rootIdx]
        inRight = B[rootIdx+1:]
        
        sLeft = set(inLeft)
        sRight = set(inRight)
        
        
        
        root.left = self.buildTree([a for a in A if a in sLeft], B[:rootIdx])
        root.right = self.buildTree([a for a in A if a in sRight], B[rootIdx+1:])
        
        return root