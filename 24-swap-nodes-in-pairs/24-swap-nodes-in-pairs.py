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
        def swap(head):
            if not head or not head.next:
                return head
            p1=head
            p2=head.next
            p3=p2.next
            
            p1.next=p3
            p2.next=p1
            
            if p3:
                p1.next=swap(p3)
            
            return p2
        
            
            
        return  swap(head)
       
#         if head and head.next:
#             tmp = head.next
#             head.next = self.swapPairs(tmp.next)
#             tmp.next = head
#             return tmp
#         return head
            
            
            
                
            