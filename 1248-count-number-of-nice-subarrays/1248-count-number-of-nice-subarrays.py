class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res=0
        count=0
        oddMap={0:1} # mapping count of odd to number of times it occured
        
        for num in nums:
            
            if num%2:
                count+=1
            if count-k in oddMap: 
                res+=oddMap[count-k]
            oddMap[count]=oddMap.get(count,0)+1
            
        return res
        
        
        
        
  