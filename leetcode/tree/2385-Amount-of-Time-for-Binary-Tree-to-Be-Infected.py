# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: TreeNode | None, start: int) -> int:
        parent={}
        q=deque([root])
        target_node=None
        while q:
            node=q.popleft()
            if node.val==start:
                target_node=node
            if node.left: 
                parent[node.left]=node 
                q.append(node.left) 
            if node.right : 
                parent[node.right]=node
                q.append(node.right)
        q=deque([target_node]) 
        visited={target_node}
        time=0
        while q:
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
            if q:
                time+=1
        return time
        