# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        stack = []
        curr = A
        
        # Initiate Stack
        while curr:
            stack.append(curr)
            curr = curr.left
            
        prev = None
        swp = []
        
        # ins = []
        while len(stack) != 0:
            act = stack.pop()
            curr = act.right
            
            while curr:
                stack.append(curr)
                curr = curr.left

            val = act.val

            if prev and prev > val:
                swp.append(prev)
                swp.append(val)
                
            prev = val   
                
        
        # print(ins)
        return min(swp), max(swp)
            
            
