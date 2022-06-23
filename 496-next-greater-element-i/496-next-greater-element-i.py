class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums2[j]==nums1[i]:
                    n=j
                    break
            k=n+1
            while k<len(nums2) :
                if nums2[k]>nums1[i]:
                    ans.append(nums2[k])
                    break  
                k+=1
            else:
                ans.append(-1)
        return ans
                        
                            
                
        