
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
#             stack = []
#             curr = 0
#             ope = "+"

#             if not s:
#                 return 0

#             operators = {'+','-','*','/'}
#             nums = set(str(x) for x in range(0,10))

#             for i in range(0,len(s)):
#                 char = s[i]

#                 if char in nums:
#                     curr = curr * 10 + int(char)

#                 if char in operators or i == len(s)-1:
#                     if ope == '+':
#                         stack.append(curr)

#                     elif ope == '-':
#                         stack.append(-curr)

#                     elif ope == '*':
#                         stack[-1] *= curr

#                     elif ope == '/':
#                         stack[-1] = int(stack[-1] / curr)

#                     curr = 0
#                     ope = char

#             return sum(stack)
