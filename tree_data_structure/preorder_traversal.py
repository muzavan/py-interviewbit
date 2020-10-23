# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def preorderTraversal(self, A):
        res = []
        if not A:
            return res
            
        stack = [A]
        
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

        return res
