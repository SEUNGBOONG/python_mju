class Node: #리스트의 각 원소를 표현하는 클라스
    def __init__(self, data):
        self.data = data
        self.next = None
class SortedLinkedList:
    def __init__(self):
        self.head = None
    def insert(self, data):
        new_node = Node(data)
# If the list is empty or the new node data is smaller than the head data

        if not self.head or data < self.head.data:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next and current.next.data < data:
            current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self): # 리스트의 원소를 프린트하는 메소드
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")