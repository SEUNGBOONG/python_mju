#1번
from queue import Queue
class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()
    def push(self, data):
        self.queue1.put(data)
        while not self.queue2.empty():
            self.queue1.put(self.queue2.get())
        self.queue1, self.queue2 = self.queue2, self.queue1
    def pop(self):
        if not self.queue2.empty():
            return self.queue2.get()
        else:
            return None


stack = StackUsingQueues()
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.pop())