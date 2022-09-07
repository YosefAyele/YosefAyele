# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res=[]
        level=[]
        
        visited=deque()
        visited.append(root)
        
        while visited:
            
                l=len(visited)
                for _ in range(l):
                    curr=visited[0]
                    if curr.left : visited.append(curr.left)
                    if curr.right: visited.append(curr.right)
                    level.append(visited.popleft().val)
                res.append(level)
                level=[]

            
        return res
        
        