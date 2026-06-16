class MinStack:
    # solution: build in the minimum into the stack

    def __init__(self):
        self.stack=[]
        self.min = float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.stack.append(0) # push the difference
            self.min = val
        else:
            self.stack.append(val-self.min) # push the difference
            if val < self.min:
                self.min = val
        

    def pop(self) -> None:
        if not self.stack:
            return

        pop = self.stack.pop()
        if pop < 0: # if value is negative, the popped element was the minimum
            self.min = self.min - pop
        

    def top(self) -> int:
        top = self.stack[-1]
        if top > 0:
            return top + self.min
        else:
            return self.min
        

    def getMin(self) -> int:
        return self.min
        
