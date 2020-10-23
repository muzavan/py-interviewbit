# Definition for a  binary tree node
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

def inOrder(n, tree):
    if not tree:
        return []
        
    return inOrder(n+1, tree.left) + [(n, tree)] + inOrder(n+1, tree.right)
class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        ins = inOrder(0, root)
        d = {}
        
        for k, v in ins:
            if k not in d:
                d[k] = []
                
            d[k].append(v)
        
        for vs in d.values():
            l = len(vs)
            i = 0
            
            while i < l - 1:
                vs[i].next = vs[i+1]
                i += 1
                
        
        return
        
