class Tree:
    def __init__(self, idx, score):
        self.idx = idx
        self.score = score
        self.left = None
        self.right = None
        
    def insert(self, node):
        if node.score > self.score:
            if self.right is None:
                self.right = node
            else:
                self.right.insert(node)
                
            return
        
        if self.left is None:
            self.left = node
        else:
            self.left.insert(node)
            
        return
    
    def order(self):
        res = []
        
        left, right = [], []
        
        if self.left:
            left = self.left.order()
            
        if self.right:
            right = self.right.order()
        
        res.extend(right)
        res.append(self.idx)
        res.extend(left)
        return res
        

class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of integers
    def solve(self, A, B):
        goods = set(A.split("_"))
        
        tree = None
        
        for i, b in enumerate(B):
            sc = self.score(b, goods)
            node = Tree(i, sc)
            
            if tree is None:
                tree = node
            else:
                tree.insert(node)
                
        
        return tree.order()
    
    
    def score(self, review, goods):
        rs = review.split("_")
        cnt = len([1 for r in rs if r in goods])
        return cnt
        
