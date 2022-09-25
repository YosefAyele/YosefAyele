from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        
        res=[]
        for num in count:
            if count[num]>int(len(nums)/3):
                res.append(num)
        
        return res