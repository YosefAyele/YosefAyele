class CustomStack:

    def __init__(self, maxSize: int):
        self.max=maxSize
        self.top=0
        self.count=0
        self.stack=[]

    def push(self, x: int) -> None:
        if self.count==self.max:
            return
        self.stack.append(x)
        self.count+=1
    def pop(self) -> int:
        if self.count==0:
            return -1
        else:
            popped=self.stack.pop()
            self.count-=1
        return popped
    def increment(self, k: int, val: int) -> None:
        if self.count>=k:
            for element in range(k):
                self.stack[element]= self.stack[element]+val
        else:
            for elements in range(self.count):
                self.stack[elements]= self.stack[elements]+val
                
            
            
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)