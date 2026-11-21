# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode | None) -> list[list[int]]:
        if not root:
            return []
        q=deque([(root,0,0)])
        d={}
        while q:
            node,row,col=q.popleft()
            if col not in d:
                d[col]=[]
            d[col].append((row,node.val))
            if node.left:
                q.append((node.left,row+1,col-1))
            if node.right:
                q.append((node.right,row+1,col+1))
        ans=[]
        for col in sorted(d):
            d[col].sort()
            values=[]
            for row,val in d[col]:
                values.append(val)
            ans.append(values)
        return ans

        