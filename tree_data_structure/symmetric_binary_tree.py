# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isSymmetric(self, A):
        if A is None:
            return 1
            
        # l = self.preOrder(A.left)
        # r = self.postOrder(A.right)
        
        # ll = len(l)
        # lr = len(r)
        # if ll != lr:
        #     return 0
        
        # i = 0
        # while i < ll:
        #     if l[i] != r[lr-1-i]:
        #         return 0
        #     i += 1
            
        return 1 if self.isSame(A.left, A.right) else 0
        
    def isSame(self, left, right):
        if left is None and right is None:
            return 1
            
        if left is None or right is None:
            return 0
        
        return (left.val == right.val) and self.isSame(left.left, right.right) and self.isSame(left.right, right.left)
        
    def preOrder(self, tree):
        if tree is None:
            return []
            
        val = tree.val
        
        left = self.preOrder(tree.left)
        right = self.preOrder(tree.right)
        
        return [val] + left + right
        
    def postOrder(self, tree):
        if tree is None:
            return []
            
        val = tree.val
        
        left = self.postOrder(tree.left)
        right = self.postOrder(tree.right)
        
        return left + right + [val]
    
    
