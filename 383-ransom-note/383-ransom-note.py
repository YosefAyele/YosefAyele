from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        ransom=Counter(ransomNote)
        mag=Counter(magazine)
        
        for i in ransom:
            if i not in mag:
                return False
            if ransom[i]>mag[i]:
                return False
        return True