# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.s = []
        self.root = root
        curr = root
        
        while curr:
            self.s.append(curr)
            curr = curr.left
 
    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return len(self.s) != 0
        
 
    # @return an integer, the next smallest number
    def next(self):
        if self.root is None:
            return None
            
        ins = self.s.pop()
        
        # next, we need to inspect the right node value.
        r = ins.right
        while r:
            self.s.append(r)
            r = r.left
        return ins.val
        
        
 
# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print i.next(),