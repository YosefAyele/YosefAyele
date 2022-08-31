# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        res=[]
        size=0
        
        temp=head
        while temp:
            size+=1
            temp=temp.next
            
        output=[0]*size
        curr=head
        
        for i in range(size):
            while res and curr.val> res[-1][1]:
                popped=res.pop()
                output[popped[0]]=curr.val
                
            res.append((i,curr.val))
            curr=curr.next
            
        return output
        