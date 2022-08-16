class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        windowsm=sum(nums[:k])
        maxav=windowsm/k
        for i in range(len(nums)-k):
            windowsm=windowsm-nums[i]+nums[i+k]
            av=windowsm/k
            maxav=av if av>maxav else maxav
        return maxav
        