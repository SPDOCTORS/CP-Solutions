# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parent={}
        q=deque([root])
        while q:
            node=q.popleft()
            if node.left:
                parent[node.left]=node
                q.append(node.left)
            if node.right:
                parent[node.right]=node
                q.append(node.right)
        visited=set()
        q=deque([target])
        visited.add(target)
        distance=0
        while q:
            if distance==k:
                break
            for i in range(len(q)):
                node=q.popleft()
                if node.left and node.left not in visited:
                    q.append(node.left)
                    visited.add(node.left)
                if node.right and node.right not in visited:
                    q.append(node.right)
                    visited.add(node.right)
                pare=parent.get(node)
                if pare and pare not in visited:
                    q.append(pare)
                    visited.add(pare)
            distance+=1
        return [node.val for node in q]


        