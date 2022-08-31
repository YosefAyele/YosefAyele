# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        
        res=[]
        output=[]
        i=0
        
        temp=head
        while temp:
            output.append(0)
            currval=temp.val
            
            while res and currval> res[-1][1]:
                popped=res.pop()
                output[popped[0]]=currval
                
            res.append((i,currval))
            temp=temp.next
            i+=1
        return output
        