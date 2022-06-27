class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        monstack=[]
        output=[0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while monstack and temperatures[i]>temperatures[monstack[-1]]:
                prev=monstack.pop()
                output[prev]=i-prev
            monstack.append(i)
        return output