# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def isBalanced(self, A):
        _, balanced = self.level(A)
        
        return 1 if balanced else 0
    
    def level(self, tree):
        if tree.left is None and tree.right is None:
            return 1, True
        
        ll, ld = 0, True
        if tree.left:
            ll, ld = self.level(tree.left)
            
        rl, rd = 0, True
        if tree.right:
            rl, rd = self.level(tree.right)
            
        balanced = (max(ll, rl) - min(ll, rl)) <= 1
        balanced = balanced and ld and rd
        lvl = max(ll, rl) + 1
        return lvl, balanced
