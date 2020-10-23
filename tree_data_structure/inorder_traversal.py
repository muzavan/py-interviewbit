# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def inorderTraversal(self, A):
        lst = []
        stack = []
        
        curr = A
        
        while curr:
            stack.append(curr)
            curr = curr.left
            
        
        while len(stack) > 0:
            act = stack.pop()
            
            curr = act.right
            while curr:
                stack.append(curr)
                curr = curr.left
            
            lst.append(act.val)
        
        return lst
