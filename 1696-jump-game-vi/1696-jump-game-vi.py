class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        
        monq=deque([0])
        
        for j in range(1,len(nums)):
            
            if  monq and j-k>monq[0]:
                monq.popleft()

            nums[j]+=nums[monq[0]]

            while monq and nums[j]>nums[monq[-1]]:
                monq.pop()
                
            monq.append(j)
                
          

        return nums[-1]
           
        