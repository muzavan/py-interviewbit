# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

MOD = 10**3 + 3
class Solution:
    # @param A : root node of tree
    # @return an integer
    def sumNumbers(self, A):
        sms = self.pathSums(0, A)
        
        res = 0
        for sm in sms:
            res += sm
            res %= MOD
        
        return res
    
    def pathSums(self, prefix, A):
        if not A.left and not A.right:
            sm = prefix * 10 + A.val
            return [sm]
            
        prefix = prefix * 10 + A.val
        sms = []
        if A.left:
            sms.extend(self.pathSums(prefix, A.left))
            
        if A.right:
            sms.extend(self.pathSums(prefix, A.right))
            
        return sms
