class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        res=len(nums)+1
        

        q=deque()
        curr=-len(nums)-1
        summ=0
        for j in range(len(nums)):
            summ+=nums[j]
            if summ>=k:
                res=min(res,j+1)
                
            while q and summ-q[0][0]>=k:
                curr=q.popleft()[1]
            res=min(res,j-curr)
            while q and summ<=q[-1][0]:
                q.pop()
                
            q.append([summ,j])     
        return res if res<len(nums)+1 else -1
    