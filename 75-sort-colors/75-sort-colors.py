class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1):
            minn=i
            for j in range(i+1,len(nums)):
                if nums[j]<nums[minn]:
                    minn=j
            if minn!=i:
                nums[minn],nums[i]=nums[i],nums[minn]
        