# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        # Traverse the original node and create map between original
        # And the cloned node
        mem = {}
        queue = [node]
        
        root = None
        while queue:
            q = queue.pop(0)
            
            clone = UndirectedGraphNode(q.label)
            
            if root is None:
                root = clone
                
            mem[q] = clone
            
            for n in q.neighbors:
                if n in mem:
                    continue
                
                queue.append(n)
                
        
        # Register the neighbors in each node
        visited = set()
        queue = [node]
        while queue:
            q = queue.pop(0)
            visited.add(q)
            
            curr = mem[q]
            for n in q.neighbors:
                clone = mem[n]
                curr.neighbors.append(clone)
                
                if n in visited:
                    continue
                
                visited.add(n)
                queue.append(n)
                
        return root