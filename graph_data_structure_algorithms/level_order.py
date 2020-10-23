# Definition for a  binary tree node
# class TreeNode:
#    def __init__(self, x):
#        self.val = x
#        self.left = None
#        self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        st = []
        res = {}
        
        st = [(0, A)]
        
        while len(st) > 0:
            info = st.pop(0)
            lvl, node = info
            
            if node is None:
                continue
            
            if lvl not in res:
                res[lvl] = []
                
            res[lvl].append(node.val)
            
            st.append((lvl+1, node.left))
            st.append((lvl+1, node.right))
        
        ks = sorted(res.keys())
        
        act = []
        for k in ks:
            act.append(res[k])
        return act
