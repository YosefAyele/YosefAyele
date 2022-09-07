# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        global answer
        
        answer=0
        
        def helper(root, depth):
            global answer
            if not root: return 
            
            if not root.right and not root.left:

                answer= max(answer,depth)
            
            helper(root.left,depth+1)
            helper(root.right,depth+1)
            
        helper(root,1)
        
        return answer
            