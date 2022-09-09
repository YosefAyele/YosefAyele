class Solution:
    def countVowels(self, word: str) -> int:
        
        res=0
        n=len(word)
        vowels=["a","e","i","o","u"]
        
        for i in range(n):
            if word[i] in vowels:
                res+=(i+1)*(n-i)
                
        return res
            
            
            