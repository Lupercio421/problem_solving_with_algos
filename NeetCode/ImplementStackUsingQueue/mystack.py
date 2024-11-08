class MyStack:
    def __init__(self):
        self.q=[]

    def push(self, x: int) -> None:
        self.q.append(x)
        for i in range(len(self.q)-1):
            self.q.append(self.q.pop(0))
        print(self.q[len(self.q)-1])

    def pop(self) -> int:
        return self.q.pop(0)

    def top(self) -> int:
        print(str(self.q[0]))
        return self.q[0]

    def empty(self) -> bool:
        if len(self.q)==0:
            print("True")
            return True
        print("False")
        return False

obj = MyStack()
obj.push(1)
obj.push(2)
obj.top()
obj.pop()
obj.empty()