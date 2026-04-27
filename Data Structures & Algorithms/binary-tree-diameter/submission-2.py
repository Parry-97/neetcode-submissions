# Definition for a binary tree node.
# class TreeNode:
#     
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_depth = self.maxDepth(root.left) if root.left else 0
        right_depth = self.maxDepth(root.right) if root.right else 0

        self.max_result = max(self.max_result, left_depth + right_depth)
        return 1 + max(left_depth, right_depth)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_result = 0
        if not root:
            return 0
        self.maxDepth(root)
        return self.max_result