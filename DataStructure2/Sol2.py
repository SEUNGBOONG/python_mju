# ListNode 클래스 정의: 연결 리스트의 노드를 나타냄
class ListNode:
    def __init__(self, newItem, nextNode: 'ListNode'):
        self.item = newItem  # 노드의 데이터(값)
        self.next = nextNode  # 다음 노드를 가리키는 포인터


# LinkedListBasic 클래스 정의
class LinkedListBasic:
    def __init__(self):
        self.__head = ListNode('dummy', None)  # 더미 헤드 노드를 가지는 연결 리스트 시작
        self.__numItems = 0  # 연결 리스트 내의 항목 수

    # 리스트에 항목 추가
    def insert(self, i: int, newItem):
        if i >= 0 and i <= self.__numItems:
            prev = self.__getNode(i - 1)  # 인덱스 i 직전의 노드를 찾음
            newNode = ListNode(newItem, prev.next)  # 새 노드 생성
            prev.next = newNode  # 이전 노드가 새 노드를 가리키도록 함
            self.__numItems += 1  # 항목 수 증가
        else:
            print("index", i, ": out of bound in insert()")  # 인덱스 범위 초과 에러 출력

    # 리스트의 끝에 항목 추가
    def append(self, newItem):
        prev = self.__getNode(self.__numItems - 1)  # 마지막 노드를 찾음
        newNode = ListNode(newItem, prev.next)  # 새 노드 생성
        prev.next = newNode  # 이전 노드가 새 노드를 가리키도록 함
        self.__numItems += 1  # 항목 수 증가

    # 리스트에서 인덱스 i의 항목을 삭제하고 반환
    def pop(self, i: int):
        if i >= 0 and i <= self.__numItems - 1:
            prev = self.__getNode(i - 1)  # 인덱스 i 직전의 노드를 찾음
            curr = prev.next  # 삭제할 노드
            prev.next = curr.next  # 이전 노드가 삭제된 노드 다음 노드를 가리키도록 함
            retItem = curr.item  # 삭제된 항목 저장
            self.__numItems -= 1  # 항목 수 감소
            return retItem  # 삭제된 항목 반환
        else:
            return None  # 인덱스 범위 초과시 None 반환

    # 리스트에서 값 x를 삭제하고 반환
    def remove(self, x):
        (prev, curr) = self.__findNode(x)  # 값 x를 가진 노드와 이전 노드를 찾음
        if curr is not None:
            prev.next = curr.next  # 이전 노드가 삭제된 노드 다음 노드를 가리키도록 함
            self.__numItems -= 1  # 항목 수 감소
            return x  # 삭제된 값 반환
        else:
            return None  # 값 x를 찾지 못하면 None 반환

    # 리스트에서 인덱스 i의 항목을 반환
    def get(self, i: int):
        if self.isEmpty():
            return None  # 리스트가 비어있으면 None 반환
        if i >= 0 and i <= self.__numItems - 1:
            return self.__getNode(i).item  # 인덱스 i의 항목 반환
        else:
            return None  # 인덱스 범위 초과시 None 반환

    # 리스트에서 값 x의 첫 번째 등장 위치(인덱스)를 반환
    def index(self, x) -> int:
        curr = self.__head.next
        for index in range(self.__numItems):
            if curr.item == x:
                return index  # 값을 찾으면 인덱스 반환
            else:
                curr = curr.next
        return -2  # 값을 찾지 못하면 -2 반환

    # 리스트가 비어있는지 여부를 반환
    def isEmpty(self) -> bool:
        return self.__numItems == 0

    # 리스트의 항목 수를 반환
    def size(self) -> int:
        return self.__numItems

    # 리스트를 비움
    def clear(self):
        self.__head = ListNode("dummy", None)  # 더미 헤드 노드로 초기화
        self.__numItems = 0  # 항목 수 초기화

    # 값 x의 등장 횟수를 반환
    def count(self, x) -> int:
        cnt = 0
        curr = self.__head.next
        while curr is not None:
            if curr.item == x:
                cnt += 1  # 값을 찾을 때마다 카운트 증가
            curr = curr.next
        return cnt  # 등장 횟수 반환

    # 리스트에 다른 리스트 a의 항목을 추가
    def extend(self, a):
        for index in range(a.size()):
            self.append(a.get(index))  # 리스트 a의 항목을 현재 리스트 끝에 추가

    # 현재 리스트의 복사본을 반환
    def copy(self):
        a = LinkedListBasic()  # 빈 리스트 a 생성
        for index in range(self.__numItems):
            a.append(self.get(index))  # 현재 리스트의 항목을 리스트 a에 추가
        return a  # 리스트 a를 반환

    # 리스트의 항목 순서를 뒤집음
    def reverse(self):
        a = LinkedListBasic()  # 빈 리스트 a 생성
        for index in range(self.__numItems):
            a.insert(0, self.get(index))  # 현재 리스트의 항목을 역순으로 리스트 a에 추가
        self.clear()  # 현재 리스트 비움
        for index in range(a.size()):
            self.append(a.get(index))  # 리스트 a의 항목을 현재 리스트에 추가

    # 리스트의 항목을 정렬
    def sort(self) -> None:
        a = []
        for index in range(self.__numItems):
            a.append(self.get(index))  # 현재 리스트의 항목을 리스트 a에 추가
        a.sort()  # 리스트 a 정렬
        self.clear()  # 현재 리스트 비움
        for index in range(len(a)):
            self.append(a[index])  # 정렬된 리스트 a의 항목을 현재 리스트에 추가

    # 리스트의 항목을 출력
    def printList(self):
        curr = self.__head.next
        while curr is not None:
            print(curr.item, end=' ')
            curr = curr.next
        print()  # 모든 항목 출력 후 줄 바꿈

    # 값 x를 가진 노드와 그 이전 노드를 찾아 반환
    def __findNode(self, x):
        prev = self.__head
        curr = prev.next
        while curr is not None:
            if curr.item == x:
                return (prev, curr)  # 값을 찾으면 이전 노드와 현재 노드 반환
            else:
                prev = curr
                curr = curr.next
        return (None, None)  # 값을 찾지 못하면 (None, None) 반환

    # 인덱스 i의 노드를 찾아 반환
    def __getNode(self, i: int):
        curr = self.__head
        for index in range(i + 1):
            curr = curr.next
        return curr  # 인덱스 i의 노드 반환

    def printInterval(self, p: int, q: int):
        if p < 0 or q >= self.__numItems or p > q:
            print("범위초과 출력 불가능합니다.")
        else:
            curr = self.__getNode(p)
            for i in range(p, q + 1):
                print(curr.item, end=' ')
                curr = curr.next
            print()

        # 예시 리스트 생성


list = LinkedListBasic()
list.append(1)
list.append(2)
list.append(3)
list.append(4)
list.append(5)
list.append(6)

# printInterval 메서드 호출
list.printInterval(2, 5)  # 범위에 해당하는 원소 출력

# 범위 초과 메시지 출력
list.printInterval(2, 100)