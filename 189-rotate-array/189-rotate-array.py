class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)

        res=[0]*s
        
        
        for i in range(s):
            res[(i+k)%s]=nums[i]

    
        for i in range(s): nums[i]=res[i]
        
        
    
        
    