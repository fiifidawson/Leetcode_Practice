class MyStack:

    def __init__(self, deque):
        self.queue = deque()
        

    def push(self, x: int) -> None:
        self.queue.append(x)
        

    def pop(self) -> int:
        # # pop right most element
        # return self.queue.pop()
        """This is a method definition for pop(). It returns an integer. It first initializes a 
        loop over a range of indices from 0 to len(self.queue) - 1. Within each iteration of the loop,
        the method calls push() to add the leftmost element in self.queue to the right end of the queue,
        effectively reversing the order of the elements. After the loop, it returns the leftmost element 
        in self.queue, which is effectively the rightmost element of the original queue."""
        for i in range(len(self.queue) - 1):
            self.push(self.queue.popleft())
        return self.queue.popleft()     

    def top(self) -> int:
        # return right most element
        self.queue[-1]        

    def empty(self) -> bool:
        return len(self.queue) == 0
        