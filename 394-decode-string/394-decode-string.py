class Solution:
    '''def decodeString(self, s: str) -> str:
        stack=[]
        size=len(s)
        output=""
        for i in range(size):
            if s[i]=="]":
                collect=""
                i=1
                k=0
                while stack[-1]!="[":
                    collect=stack.pop()+collect
                else:
                    stack.pop()
                while  len(stack)!=0 and stack[-1].isdigit():
                    k+=int(stack.pop())*i
                    i*=10
                stack.append(k*collect)
            else:
                stack.append(s[i])
        for val in stack:
            output+=val
        return output'''
    
  
