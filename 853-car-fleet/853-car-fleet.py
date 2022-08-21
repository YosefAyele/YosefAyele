class Solution:
    def carFleet(self, tar: int, position: List[int], sp: List[int]) -> int:
        pos=[]
        for i in range(len(position)):
            pos.append([position[i],sp[i]])
        pos.sort(reverse=True)
#         print(pos)
        monstack=[]
        
        for pair in pos:
            
            currtime=(tar-pair[0])/pair[1]
            # print(monstack)
            
            if monstack and currtime<=monstack[-1]:
                currtime=monstack.pop()
            
            monstack.append(currtime)
        return len(monstack)
            
        