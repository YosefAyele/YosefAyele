# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        # l l   l r
        # F F F T T
        # 1,2,3,4,5
        
        low=1
        high=n
        ans = -1
        
        while low<=high:
            mid=(low+high)//2
            if isBadVersion(mid):
                ans = mid
                high=mid-1
            else:
                low=mid+1
        return ans
                