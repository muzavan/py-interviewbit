# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def flatten(self, A):
        return self.process(A)
    
    def process(self, root):
        if not root:
            return None
            
        curr = root
        left = curr.left
        right = curr.right
        
        fltLeft = self.process(left)
        fltRight = self.process(right)
        
        curr.left = None
        curr.right = fltLeft
        
        while curr.right:
            curr = curr.right
            
        curr.right = fltRight
        
        return root
        
    
    
