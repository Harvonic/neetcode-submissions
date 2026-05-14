# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # find the path to a node with value
        def findPath(root, value):
            path = []
            current = root

            while current:
                path.append(current)

                if current.val < value:
                    current = current.right
                elif current.val > value:
                    current = current.left
                else:
                    break

            return path
        

        ppath = findPath(root, p.val)
        qpath = findPath(root, q.val)

        seen = {}

        for i in ppath:
            seen[i] = True

        common = root
        for i in range(len(qpath) - 1, -1, -1):
            if qpath[i] in seen:
                common = qpath[i]
                break
        
        return common
        

    
        