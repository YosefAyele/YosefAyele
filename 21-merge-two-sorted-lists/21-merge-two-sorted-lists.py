# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, h1: Optional[ListNode], h2: Optional[ListNode]) -> Optional[ListNode]:
        
        res=ListNode()
        restail=res
        
        while h1 and h2:
            
            if h1.val<=h2.val:
                restail.next=h1
                h1=h1.next
    
            else:
                restail.next=h2
                h2=h2.next
                
            restail=restail.next
                
        if h1 or h2:
            restail.next=h1 if h1 else h2
                
        return res.next
    
    
    