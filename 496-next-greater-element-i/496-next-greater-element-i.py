class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        mapp={i:-1 for i in nums1}
           
        monstack=[]
        
        for i in nums2:
            
            while monstack and i>monstack[-1]:
                mapp[monstack[-1]]=i
                monstack.pop()
            monstack.append(i)
        return [mapp[i] for i in nums1]