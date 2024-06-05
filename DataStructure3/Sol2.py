#2번
from queue import Queue


class Queue:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, element):
        self.in_stack.append(element)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) > 0:
                self.out_stack.append(self.in_stack.pop())

        return self.out_stack.pop()

    def is_empty(self):
        return len(self.in_stack) == 0 and len(self.out_stack) == 0


# enqueue는 새로운 요소를 추가한다.
# dequeue는 빈 out_stack에 in_stack 요소를 꺼내어 역순으로 넣고
# 그후에 pop하여 반환한다. 그래서 FIFO형식으로 나가게된다.

# 두 스택을 사용하여 큐를 구현하면 enqueue는 연산이 상대적으로 빠르게 이루어지지만
#dequeue 연사에서는 역순으로 바꾸는 작업이 필요하므로 상대적으로 느리다.