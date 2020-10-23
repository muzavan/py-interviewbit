# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, A, B, C):
        bPath = self.findPath([], A, B)
        cPath = self.findPath([], A, C)
        
        parent = -1
        for a, b in zip(bPath, cPath):
            if a != b:
                break
            parent = a
        return parent
    
    def findPath(self, prefix, A, B):
        if not A:
            return []
            
        pr = prefix + [A.val]
        if A.val == B:
            return pr
            
        left = self.findPath(pr, A.left, B)
        
        if len(left) > 0:
            return left
            
        return self.findPath(pr, A.right, B)
