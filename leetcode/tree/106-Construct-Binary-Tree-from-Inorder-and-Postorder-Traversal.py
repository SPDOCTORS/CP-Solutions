# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode | None:
        i = len(postorder) - 1

        def build(left, right):
            nonlocal i

            if left > right:
                return None

            root_val = postorder[i]
            i -= 1

            root = TreeNode(root_val)

            root_index = inorder.index(root_val)

            root.right = build(root_index + 1, right)
            root.left = build(left, root_index - 1)

            return root

        return build(0, len(inorder) - 1)
        