# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        if not root: return True
        
        def check(left,right):
            
            if not left or not right:
                return left==right
            
            if left.val!=right.val:
                return False
            
            return check(left.left,right.right) and check(left.right,right.left)
            
        val=check(root.left,root.right)
        
        return val