# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        size=0
        while temp:
            temp=temp.next
            size+=1
        temp=head
        for i in range(size//2):
            temp=temp.next
        return temp
            

            
        