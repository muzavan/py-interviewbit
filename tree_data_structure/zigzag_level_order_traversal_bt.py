# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def zigzagLevelOrder(self, A):
        ins = self.inOrder(0, A)
        if len(ins) == 0:
            return []
            
        mxLevel = max([a[0] for a in ins])
        
        reverse = False
        res = []
        for i in range(mxLevel+1):
            ls = [a[1] for a in ins if a[0] == i]
            if reverse:
                ls = ls[::-1]
            
            res.append(ls)
            reverse = not reverse
            
        return res
    
    def inOrder(self, lvl, A):
        if not A:
            return []
            
        return self.inOrder(lvl+1, A.left) + [(lvl, A.val)] + self.inOrder(lvl+1, A.right)
