class MinStack:

    def __init__(self):
        self.stack=[]
        self.minstack=[]
        self.min=None

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            self.stack.append(val)
            if self.top() < self.minstack[-1]:
                self.minstack.append(val)
            else:
                self.minstack.append(self.minstack[-1])
            

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()