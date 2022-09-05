# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        
        curr=root
        stack=[]
        
        while curr or stack:
            
            while curr:
                stack.append(curr)
                curr=curr.left
            curr=stack.pop()
            output.append(curr.val)
            curr=curr.right
        return output
        
        
        
        
        
        
        # recursive solution
        def helper(root,inorderList):
            
            if not root: return 
            
            helper(root.left,inorderList)
            inorderList.append(root.val)
            helper(root.right,inorderList)
            
        helper(root,output)
                
        return output
