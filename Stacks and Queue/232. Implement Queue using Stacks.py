class MyQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []
        

    def push(self, x: int) -> None:
        return self.stack_in.append(x)
       

    def pop(self) -> int:
        if not self.stack.out:
            self.stack_out = self.stack_in[::-1]

            return self.stack_out.pop()
    
        

    def peek(self) -> int:
         if not self.stack.out:
            self.stack_out = self.stack_in[::-1]

            return self.stack_out.top()
        

    def empty(self) -> bool:
        if not self.stack_in and self.stack_out:
            return True
        