# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return [True, 0]

            right_balanced, right_depth = dfs(root.right)
            left_balanced, left_depth = dfs(root.left)

            balanced = (
                right_balanced and left_balanced and abs(left_depth - right_depth) <= 1
            )

            depth = max(left_depth, right_depth) + 1

            if balanced:
                return [True, depth]
            else:
                return [False, depth]

        return dfs(root)[0]