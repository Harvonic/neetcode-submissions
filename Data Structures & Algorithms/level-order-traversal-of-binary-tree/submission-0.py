# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:


        res = []
        queue = []

        if root:
            queue.append(root)
        
        while queue:
            temp = []

            while queue:
                temp.append(queue.pop(0))
            
            res.append([i.val for i in temp])
            
            while temp:
                popped = temp.pop(0)
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)
        
        return res