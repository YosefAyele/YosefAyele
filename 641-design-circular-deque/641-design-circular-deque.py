class MyCircularDeque:

    def __init__(self, k: int):
        self.k=k
        self.path=[-1]*k
        self.f,self.r=0,0
        self.size=0
    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.path[self.f]=value
        else:
            self.f=(self.f-1)%self.k
            self.path[self.f]=value
        self.size+=1
        return True
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.isEmpty():
            self.path[self.r]=value
        else:
            self.r=(self.r+1)%self.k
            self.path[self.r]=value
        self.size+=1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.path[self.f]=-1
        self.f=(self.f+1)%self.k
        self.size-=1
        if self.isEmpty():
             self.r=self.f
        return True
            
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.path[self.r]=-1
        self.r=(self.r-1)%self.k
        self.size-=1
        if self.isEmpty():
            self.f=self.r
        return True
        

    def getFront(self) -> int:
        return self.path[self.f]
        

    def getRear(self) -> int:
        return self.path[self.r]
        

    def isEmpty(self) -> bool:
        return self.size==0
        

    def isFull(self) -> bool:
        return self.size==self.k
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()