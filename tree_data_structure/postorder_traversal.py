# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def postorderTraversal(self, A):
        res = []
        if not A:
            return res
        
        curr = A
        stack = [curr]
        
        while len(stack) > 0:
            curr = stack.pop()
            res.append(curr.val)
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
                    
        return res[::-1]