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
        if len(B) == 0:
            return None
            
        root = B[-1]
        i = 0
        for i, v in enumerate(A):
            if v == root:
                break
        
        inLeft = A[:i]
        inRight = A[i+1:]
        
        sLeft = set(inLeft)
        sRight = set(inRight)
        
        poLeft = []
        poRight = []
        for b in B[:-1]:
            if b in sLeft:
                poLeft.append(b)
            elif b in sRight:
                poRight.append(b)
            
        tree = TreeNode(root)
        tree.left = self.buildTree(inLeft, poLeft)
        tree.right = self.buildTree(inRight, poRight)
        
        return tree
