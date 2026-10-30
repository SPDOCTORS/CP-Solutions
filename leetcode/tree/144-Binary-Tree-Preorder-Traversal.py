# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        arr=[]
        self.recursive(root,arr)
        return arr
    def recursive(self,root,arr):
        if root is None:
            return
        arr.append(root.val)
        self.recursive(root.left,arr)
        self.recursive(root.right,arr)
        return arr

        