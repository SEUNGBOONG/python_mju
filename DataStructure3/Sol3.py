#3번

class ListQueue:
    def __init__(self):
        self.__queue = []

    def enqueue(self,x):
        self.__queue.append(x)##-> self.__queue.insert(0,x) 수정해야됨

    def dequeue(self):
        return self.__queue.pop(0) # return self.__queue.pop()으로 수정
    def front(self):
        if self.inEmpty():
            return None
        else :
            return self.__queue[0]  #return self.__queue[-1] 로수정

    def isEmpty(self) -> bool:
        return (len(self.__queue)==0):
    def dequeueAll(self):
        self.__queue.clear() #

    def dequeueAll(self):
        self.__queue.clear()

    def printQueue(self):
        print("queue from front", end= '')
        for i in range(len(self.__queue)):
            print(self.__queue[i],end ='')
        print()
