# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        
        curr=root
        stack=[]
        
        while curr or stack:
            
            if curr:
                
                stack.append(curr)
                output.append(curr.val)
                curr=curr.right
            else:
                curr=stack.pop().left
        return output[::-1]
            
            
        
        
        
        def postorder(root,res):
            if not root: return 
            
            postorder(root.left,res)
            postorder(root.right,res)
            res.append(root.val)
            
        postorder(root,output)
        
        return output
    
        
            
            
        
        