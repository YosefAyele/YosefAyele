class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        
        # '''...Brute Force Solution...'''
#         maxfreq=0
#         nums.sort(reverse=True)

#         for i in range(len(nums)):
#             j=i
#             oprtn=k
#             currfreq=0
#             while j<len(nums) and oprtn-(nums[i]-nums[j])>=0 :
#                 oprtn-=(nums[i]-nums[j])
#                 j+=1
#                 currfreq+=1
                
#             maxfreq=max(currfreq,maxfreq)
        
#         return maxfreq
    
      # '''....Sliding Window Soluiton...'''
        nums.sort()
        l=r=0
        maxfreq=0
        Total=0

        while r<len(nums):

            Total+=nums[r]
            
            while nums[r]*(r-l+1)>Total+k:
                Total-=nums[l]
                l+=1
            maxfreq=max(r-l+1,maxfreq)
                
            r+=1
        return maxfreq


            