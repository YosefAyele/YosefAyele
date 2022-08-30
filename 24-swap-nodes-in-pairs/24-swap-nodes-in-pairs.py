# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=temp=ListNode()
        dummy.next=head
        
        while head and head.next:

            nxt=head.next
            head.next=nxt.next
            nxt.next=head
            temp.next=nxt
            
            head=head.next
            temp=nxt.next
        return dummy.next
            
            
                
            