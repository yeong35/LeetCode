"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def __init__(self):
        self.visited = {}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val)
        self.visited[node] = clone_node

        for neighbor in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(neighbor))
    
        return clone_node
