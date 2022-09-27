# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def findMid(head):
            
            slow=None
            while head and head.next:
                slow=head if not slow else slow.next
                head=head.next.next
                
            
            secondhalf=slow.next
            slow.next=None
            return secondhalf
        
        def merge(h1,h2):
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
        
        def sort(head):
            if not head or not head.next: return head
            mid=findMid(head)
            left=sort(head)
            right=sort(mid)
            
            return merge(left,right)
        return sort(head)