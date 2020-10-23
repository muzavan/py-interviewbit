# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return an integer
    def maxPathSum(self, A):
        dp = {"max": -99999}
        self.maxPath(A, dp)
        return dp["max"]
    
    # Return max_value, include_root
    def maxPath(self, A, dp):
        if A is None:
            return 0
            
        maxLeft = self.maxPath(A.left, dp)
        maxRight = self.maxPath(A.right, dp)
        
        max1 = max(A.val, A.val + max(maxLeft, maxRight))
        max2 = max(max1, maxLeft + maxRight + A.val)
        
        dp["max"] = max(dp["max"], max2)
        return max1
            
