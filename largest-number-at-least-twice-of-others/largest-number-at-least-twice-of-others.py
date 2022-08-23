class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        
        maxElementIndex=nums.index(max(nums))
        nums.sort()
        print(nums)
        if nums[-1]>=2*nums[-2]:
            return maxElementIndex
        return -1