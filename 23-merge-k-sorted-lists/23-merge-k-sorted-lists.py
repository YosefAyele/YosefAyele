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
        srtd=None
        for i in range(len(lists)):
            if not lists[i]: continue
            srtd=merge(srtd,lists[i])
        
        return srtd
        
        