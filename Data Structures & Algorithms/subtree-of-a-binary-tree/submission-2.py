# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if p and q:
                if p.val != q.val:
                    return False
                
                return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
            elif p is None and q is None:
                return True
            else:
                return False
        
        # stack = []
        # stack.append(root)

        # while stack:

        #     popped = stack.pop()

        #     compared = isSameTree(popped, subRoot)

        #     if compared:
        #         return True

        #     if popped.left:
        #         stack.append(popped.left)
        #     if popped.right:
        #         stack.append(popped.right)
        
        # return False

        if not root:
            return False

        return isSameTree(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


