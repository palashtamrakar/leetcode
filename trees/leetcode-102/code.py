# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        outarr = []

        def traverse(node, n):
            if not node:
                return

            if n == len(outarr):
                outarr.append([])

            outarr[n].append(node.val)

            traverse(node.left, n + 1)
            traverse(node.right, n + 1)

        traverse(root, 0)
        return outarr
