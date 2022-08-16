class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        output=[-1]*len(nums)
        diam=2*k+1
        initial=0
        windowsm=0
        for i in range (len(nums)):
            windowsm+=nums[i]
            if i-initial+1>=diam:
                output[initial+k]=windowsm//diam
                windowsm-=nums[initial]
                initial+=1
        return output