# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        size=0
        temp=head
        while temp:
            size+=1
            temp=temp.next
        temp1=head
        currSize=0
        
        while temp1:
            if size-currSize-1==n:
                temp1.next=temp1.next.next
            temp1=temp1.next
            currSize+=1
        if n==size:
            return head.next
        return head
        
        