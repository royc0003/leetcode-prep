class MyQueue:
    
    def __init__(self):
        '''
        write_stack = [4,5]
        read_stack = [3,2,1]
        1. only when read_stack is empty, push the write_stack to read_stack ensuring 
        that the order is reversed.
        2. hanlde front of write_stack by using a self.front var, but priority of peek() should be given to read_stack.
        '''
        self.write_stack = [] 
        self.read_stack = [] 
        self.front = 0
        

    def push(self, x: int) -> None:
        if not self.write_stack:
            self.front = x
        self.write_stack.append(x)
    

    def pop(self) -> int:
        if not self.read_stack:
            while self.write_stack:
                self.read_stack.append(self.write_stack.pop())
        
        res = self.read_stack.pop()
        return res

    def peek(self) -> int:
        if self.read_stack:
            return self.read_stack[-1]
        return self.front
        

    def empty(self) -> bool:
        return len(self.read_stack) == 0 and len(self.write_stack) == 0 
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()