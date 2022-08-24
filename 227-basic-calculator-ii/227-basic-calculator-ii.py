
class Solution:
    def calculate(self, s: str) -> int:

        s=s.replace(" ","")
        
        toAdd=[]
        i=0
        num=0
        operation="+"

        while i <len(s):
            if s[i].isnumeric():
                num=(num*10) + int(s[i])
            if not s[i].isnumeric() or i==len(s)-1:
                if operation=="+":
                    toAdd.append(num)
                elif  operation=="-":
                    toAdd.append(-num)

                elif operation=="*":
                    toAdd.append(toAdd.pop()*num)
                elif operation=="/":
                    toAdd.append(int(toAdd.pop()/num))

                operation=s[i]
                num=0
            i+=1
        return sum(toAdd)

