"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if not node:
            return None
            
        created = {}
        stack = []
        stack.append(node)


        while stack:
            popped = stack.pop(0)
            new_node = created[popped.val] if popped.val in created else Node(popped.val, None)
            created[popped.val] = new_node

            for n in popped.neighbors:

                if n.val in created:
                    new_node.neighbors.append(created[n.val])
                else:
                    new = Node(n.val, None)
                    created[n.val] = new
                    new_node.neighbors.append(new)
                    stack.append(n)
        
        print(created)
        return created[1]





        