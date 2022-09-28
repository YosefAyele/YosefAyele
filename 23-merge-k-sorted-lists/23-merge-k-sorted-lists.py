# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        def merge(h1,h2):
                res=ListNode(0)
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
        
        if len(lists)==0: return None
        
        while len(lists)>1:
            merged=[]
            for i in range(0,len(lists),2):
                l1=lists[i]
                l2=lists[i+1] if i+1<len(lists) else None
                
                merged.append(merge(l1,l2))
            lists=merged
        return lists[0]
        
  
    
        
        