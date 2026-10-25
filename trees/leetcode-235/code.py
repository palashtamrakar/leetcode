# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findparent(self, root, node):
        if not root:
            return None

        if root.left == node or root.right == node:
            return root

        left = self.findparent(root.left, node)
        if left:
            return left

        return self.findparent(root.right, node)

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ancestors = set()

        curr = p
        while curr:
            ancestors.add(curr)
            curr = self.findparent(root, curr)

        curr = q
        while curr:
            if curr in ancestors:
                return curr
            curr = self.findparent(root, curr)

        return None
