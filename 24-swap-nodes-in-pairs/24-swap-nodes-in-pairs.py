# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
#         dummy=track=ListNode()
#         dummy.next=head
#         prev, curr= dummy, head
        
#         while curr and curr.next:
            
#             nxtpair=curr.next.next
#             second=curr.next
            
#             second.next=curr
#             curr.next=nxtpair
#             prev.next=second
            
#             prev=curr
#             curr=curr.next
            
#         return dummy.next
        if head and head.next:
            temp=head.next
            head.next=self.swapPairs(temp.next)
            temp.next=head
            return temp
            
        return head
       
#         if head and head.next:
#             tmp = head.next
#             head.next = self.swapPairs(tmp.next)
#             tmp.next = head
#             return tmp
#         return head
            
            
            
                
            