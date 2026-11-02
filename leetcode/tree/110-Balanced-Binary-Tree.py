# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        left=self.height(root.left)
        right=self.height(root.right)
        return 1+max(left,right)
    def isBalanced(self, root: TreeNode | None) -> bool:
        if root is None:
            return True
        leftH=self.height(root.left)
        rightH=self.height(root.right)
        if abs(leftH-rightH)>1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
        