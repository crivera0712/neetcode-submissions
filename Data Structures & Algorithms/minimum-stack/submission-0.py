class MinStack:
    #[-1,-2,1,0,3]
    def __init__(self):
        self.stack = []
        self.prefix_min = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.prefix_min) == 0: 
            self.prefix_min.append(val)
        else:
            top_val = self.prefix_min[-1]
            self.prefix_min.append(min(val,top_val))
        
    def pop(self) -> None:
        self.stack.pop()
        self.prefix_min.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix_min[-1]
