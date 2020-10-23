# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        return self.hasPath([], A, B)
    
    def hasPath(self, prefix, A, B):
        if not A.left and not A.right:
            res = []
            if A.val == B:
                res.append(prefix + [A.val])
            
            return res
            
        if not A.left:
            return self.hasPath(prefix + [A.val], A.right, B - A.val)
            
        if not A.right:
            return self.hasPath(prefix + [A.val], A.left,  B - A.val)
            
        res = []
        l = self.hasPath(prefix + [A.val],A.left, B - A.val)
        if l:
            res.extend(l)
        
        r = self.hasPath(prefix + [A.val], A.right,  B - A.val)
        if r:
            res.extend(r)
        return res
        
        