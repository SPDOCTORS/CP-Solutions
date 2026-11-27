# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        i=0
        def build(left,right):
            nonlocal i
            if left>right:
                return None
            root_val=preorder[i]
            i+=1
            root=TreeNode(root_val)
            root_index=inorder.index(root_val)
            root.left=build(left,root_index-1)
            root.right=build(root_index+1,right)
            return root
        return build(0,len(inorder)-1)
        