class Solution:
    def countCollisions(self, di: str) -> int:
        
        
        return len(di.lstrip('L').rstrip('R').replace('S',''))