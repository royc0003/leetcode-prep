class BrowserHistory:
    

    def __init__(self, homepage: str):
        
        self.history_stack = [homepage]
        self.rpointer = 0
        

    def visit(self, url: str) -> None:
        if self.rpointer < len(self.history_stack) - 1:
            self.history_stack = self.history_stack[0:self.rpointer+1]
        
        self.history_stack.append(url)
        self.rpointer = len(self.history_stack) -1

    def back(self, steps: int) -> str:
        if (self.rpointer - steps ) < 0:
            self.rpointer = 0
            return self.history_stack[self.rpointer]
        self.rpointer -= steps
        return self.history_stack[self.rpointer]


    def forward(self, steps: int) -> str:
        if (self.rpointer + steps) >= len(self.history_stack):
            self.rpointer = len(self.history_stack) - 1
            return self.history_stack[self.rpointer]
        
        self.rpointer += steps
        return self.history_stack[self.rpointer]
        
            
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)