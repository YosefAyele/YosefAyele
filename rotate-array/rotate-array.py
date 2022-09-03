class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s=len(nums)
        k=k%s
#         res=[0]*s
        
        
#         for i in range(s):
#             res[(i+k)%s]=nums[i]

    
#         for i in range(s): nums[i]=res[i]
            
        def helper(arr,i,j):
            while i<=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
            return
        helper(nums,0,s-1)
        helper(nums,0,k-1)
        helper(nums,k,s-1)
        
        
        
    
        
    