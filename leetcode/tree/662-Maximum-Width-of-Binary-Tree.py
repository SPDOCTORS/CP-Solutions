# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        q=deque([(root,0)])
        max_width=0
        while q:
            left=q[0][1]
            right=q[-1][1]
            width=right-left+1
            max_width=max(max_width,width)
            for i in range(len(q)):
                node,index=q.popleft()
                if node.left:
                    q.append((node.left,2*index+1))
                if node.right:
                    q.append((node.right,2*index+2))
        return max_width
        