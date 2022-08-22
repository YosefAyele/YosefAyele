class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        l=r=0
        winsize=0
        decQ=collections.deque()
        incQ=collections.deque()
        while r<len(nums):
            
            while decQ and nums[r]>=nums[decQ[-1]]: decQ.pop()
                
            while incQ and nums[r]<=nums[incQ[-1]]: incQ.pop()

            incQ.append(r)
            decQ.append(r)
            
            while abs(nums[decQ[0]]-nums[incQ[0]])>limit:
                l+=1
                if l > incQ[0]:
                    incQ.popleft()
                if l > decQ[0]:
                    decQ.popleft()
            winsize=max(winsize,r-l+1)
            r+=1
        return winsize
        