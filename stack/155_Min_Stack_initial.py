class MinStack:
    '''
    maintaining index of every min value
    time = O(1)
    space = O(n), and is optimised due to indexing
    '''

    def __init__(self):
        self.stack = []
        self.minIndexStack = [0] 
        

    def push(self, val: int) -> None:
        if self.stack and self.minIndexStack and val <= self.stack[self.minIndexStack[-1]]:
            self.minIndexStack.append(len(self.stack))
        self.stack.append(val)
        

    def pop(self) -> None:
        if self.minIndexStack and self.stack[-1] == self.stack[self.minIndexStack[-1]]:
            self.minIndexStack.pop()
        return self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.stack[self.minIndexStack[-1]] if self.minIndexStack else self.stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()