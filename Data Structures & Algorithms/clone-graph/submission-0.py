"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        newAdjList = {}

        def dfs(node):
            if node in newAdjList:
                return newAdjList[node]
            
            old = Node(node.val)
            newAdjList[node] = old
            for neighbor in node.neighbors:
                old.neighbors.append(dfs(neighbor))
            return old
        
        return dfs(node) if node else None