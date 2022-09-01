class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        i,j=0,len(numbers)-1
        
        while i<j:
            curSum=numbers[i]+numbers[j]
            if curSum==target:
                return [i+1,j+1]
            if curSum>target:
                j-=1
            else:
                i+=1
        
            
        