# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        output=[]
        
        def helper(root,output):
            
            if not root: return 
            
            output.append(root.val)
            
            helper(root.left,output)
            helper(root.right,output)
            
        # helper(root,output)

        curr=root
        stack=[]
        
        while curr or stack:
            if curr:
                stack.append(curr)
                output.append(curr.val)
                curr=curr.left
            else:
                curr=stack.pop().right
                
        return output
            
            