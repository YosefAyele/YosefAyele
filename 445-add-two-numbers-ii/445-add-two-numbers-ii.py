# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def reverseLL(head):
            
            prev,curr=None,head
            
            while curr:
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt
            return prev
        
        
        h1,h2=reverseLL(l1),reverseLL(l2)
        
        
        res=ListNode(0)
        restail=res
    
        carry=0
        while h1 or h2 or carry:
            val1=h1.val if h1 else 0
            val2=h2.val if h2 else 0
            
            summ=val1+val2+carry
            carry=summ//10
            
            restail.next=ListNode(summ%10)
            restail=restail.next
            
            h1=h1.next if h1 else None
            h2=h2.next if h2 else None
            
        return reverseLL(res.next)
            
        