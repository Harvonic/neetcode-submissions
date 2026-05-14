# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # if root is None:
        #     return 0
        # else:
        #     return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # non recursive - level order traversal

        if not root:
            return 0
        
        queue = []
        queue.append([1, root])
        maxd = 0

        while queue != []:
            head = queue.pop(0)
            level = head[0]
            popped = head[1]

            maxd = max(maxd, level)

            if popped.left:
                queue.append([level + 1, popped.left])
            if popped.right:
                queue.append([level + 1, popped.right])
            
        
        return maxd



        