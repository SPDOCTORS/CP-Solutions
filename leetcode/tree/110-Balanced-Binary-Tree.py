# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        def dfs(root):
            if root is None:
                return 0
            leftH=dfs(root.left)
            if leftH==-1:
                return -1
            rightH=dfs(root.right)
            if rightH==-1:
                return -1
            if abs(leftH-rightH)>1:
                return -1
            return 1+max(leftH,rightH)
        return dfs(root)!=-1
        