# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=move=ListNode(0)
        dummy.next=first=second=head
        
        while True:
            count=0
            while second and count<k:
                second=second.next
                count+=1
            if count==k:
                
                pre, curr= second, first
                
                for _ in range(k):
                    nxt=curr.next
                    curr.next=pre
                    pre=curr
                    curr=nxt
                move.next=pre
                move= first
                first=second
            else: return dummy.next
            
        
        
        
        
            