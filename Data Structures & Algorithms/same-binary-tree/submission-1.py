# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if (not root) and (not subRoot):
            return True
        if root and subRoot:
            if subRoot.val == root.val:
                return self.isSameTree(root.left, subRoot.left) and self.isSameTree(
                    root.right, subRoot.right
                )
        return False
