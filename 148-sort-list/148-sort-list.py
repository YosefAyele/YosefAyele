# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=head
        res=[]
        
        dummy=ListNode()
        trace=dummy
        while temp:
            res.append(temp.val)
            temp=temp.next
        
        res.sort()
        
        for val in res:
            node=ListNode(val)
            trace.next=node
            trace=trace.next
        return dummy.next
        