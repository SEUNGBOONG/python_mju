# ListNode 클래스 정의: 연결 리스트의 노드를 나타냄
class ListNode:
   def __init__(self, newItem, nextNode: 'ListNode'):
      self.item = newItem  # 노드의 데이터(값)
      self.next = nextNode  # 다음 노드를 가리키는 포인터

# CircularLinkedList 클래스 정의
class CircularLinkedList:
   def __init__(self):
      self.__tail = ListNode("dummy", None)  # 더미 노드를 가지는 연결 리스트 시작
      self.__tail.next = self.__tail  # 더미 노드가 자기 자신을 가리킴 (원형 리스트)
      self.__numItems = 0  # 연결 리스트 내의 항목 수

   # 리스트에 항목 추가
   def insert(self, i: int, newItem) -> None:
      if (i >= 0 and i <= self.__numItems):
         prev = self.getNode(i - 1)  # 인덱스 i 직전의 노드를 찾음
         newNode = ListNode(newItem, prev.next)  # 새 노드 생성
         prev.next = newNode  # 이전 노드가 새 노드를 가리키도록 함
         if i == self.__numItems:
            self.__tail = newNode  # 새 노드가 마지막 노드이면 tail 업데이트
         self.__numItems += 1  # 항목 수 증가
      else:
         print("index", i, ": out of bound in insert()")  # 인덱스 범위 초과 에러 출력

   # 리스트의 끝에 항목 추가
   def append(self, newItem) -> None:
      newNode = ListNode(newItem, self.__tail.next)  # 새 노드 생성
      self.__tail.next = newNode  # 이전 마지막 노드가 새 노드를 가리키도록 함
      self.__tail = newNode  # tail 업데이트
      self.__numItems += 1  # 항목 수 증가

   # 리스트에서 인덱스 i의 항목을 삭제하고 반환
   def pop(self, *args):
      # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족
      if self.isEmpty():
         return None
      # 인덱스 i 결정
      if len(args) != 0:  # pop(k)과 같이 인자가 있으면 i = k 할당
         i = args[0]
      if len(args) == 0 or i == -1:  # pop()에 인자가 없거나 pop(-1)이면 i에 맨 끝 인덱스 할당
         i = self.__numItems - 1
      # i번 원소 삭제
      if (i >= 0 and i <= self.__numItems - 1):
         prev = self.getNode(i - 1)
         retItem = prev.next.item
         prev.next = prev.next.next
         if i == self.__numItems - 1:
            self.__tail = prev
         self.__numItems -= 1
         return retItem
      else:
         return None

   # 리스트에서 값 x를 삭제하고 반환
   def remove(self, x):
      (prev, curr) = self.__findNode(x)
      if curr is not None:
         prev.next = curr.next
         if curr == self.__tail:
            self.__tail = prev
         self.__numItems -= 1
         return x
      else:
         return None

   # 리스트에서 인덱스 i의 항목을 반환
   def get(self, *args):
      # 가변 파라미터. 인자가 없거나 -1이면 마지막 원소로 처리하기 위함. 파이썬 리스트 규칙 만족
      if self.isEmpty():
         return None
      # 인덱스 i 결정
      if len(args) != 0:  # pop(k)과 같이 인자가 있으면 i = k 할당
         i = args[0]
      if len(args) == 0 or i == -1:  # pop()에 인자가 없거나 pop(-1)이면 i에 맨 끝 인덱스 할당
         i = self.__numItems - 1
      # i번 원소 리턴
      if (i >= 0 and i <= self.__numItems - 1):
         return self.getNode(i).item
      else:
         return None

   # 값 x를 가진 노드와 그 이전 노드를 찾아 반환
   def __findNode(self, x) -> (ListNode, ListNode):
      __head = prev = self.__tail.next  # 더미 헤드
      curr = prev.next  # 0번 노드
      while curr != __head:
         if curr.item == x:
            return (prev, curr)
         else:
            prev = curr
            curr = curr.next
      return (None, None)

   # 인덱스 i의 노드를 찾아 반환
   def getNode(self, i: int) -> ListNode:
      curr = self.__tail.next  # 더미 헤드, index: -1
      for index in range(i + 1):
         curr = curr.next
      return curr

   # 리스트가 비어있는지 여부를 반환
   def isEmpty(self) -> bool:
      return self.__numItems == 0

   # 리스트의 항목 수를 반환
   def size(self) -> int:
      return self.__numItems

   # 리스트를 비움
   def clear(self):
      self.__tail = ListNode("dummy", None)
      self.__tail.next = self.__tail
      self.__numItems = 0

   # 값 x의 등장 횟수를 반환
   def count(self, x) -> int:
      cnt = 0
      for element in self:
         if element == x:
            cnt += 1
      return cnt

   # 리스트에 다른 리스트 a의 항목을 추가
   def extend(self, a):  # a는 순회 가능한 모든 객체
      for x in a:
         self.append(x)

   # 리스트의 복사본을 생성하여 반환
   def copy(self) -> 'CircularLinkedList':
      a = CircularLinkedList()
      for element in self:
         a.append(element)
      return a

   # 리스트를 역순으로 변경
   def reverse(self) -> None:
      __head = self.__tail.next  # 더미 헤드
      prev = __head
      curr = prev.next
      next = curr.next
      curr.next = __head
      __head.next = self.__tail
      self.__tail = curr
      for i in range(self.__numItems - 1):
         prev = curr
         curr = next
         next = next.next
         curr.next = prev

   # 리스트를 정렬
   def sort(self) -> None:
      a = []
      for element in self:
         a.append(element)
      a.sort()
      self.clear()
      for element in a:
         self.append(element)

   # 리스트의 항목을 출력
   def printList(self) -> None:
      for element in self:
         print(element, end=' ')
      print()

   # 리스트 순회를 위한 이터레이터 생성
   def __iter__(self):
      return CircularLinkedListIterator(self)

# CircularLinkedListIterator 클래스 정의: CircularLinkedList를 순회하기 위한 이터레이터
class CircularLinkedListIterator:
   def __init__(self, alist):
      self.__head = alist.getNode(-1)  # 더미 헤드
      self.iterPosition = self.__head.next  # 0번 노드

   # 다음 원소 반환
   def __next__(self):
      if self.iterPosition == self.__head:  # 순환 끝
         raise StopIteration
      else:  # 현재 원소를 반환하면서 다음 원소로 이동
         item = self.iterPosition.item
         self.iterPosition = self.iterPosition.next
         return item

# CircularLinkedList 객체 생성
list = CircularLinkedList()
list.append(30)
list.insert(0, 20)

# 리스트 a와 확장 및 연산 수행
a = [4, 3, 3, 2, 1]
list.extend(a)
list.reverse()
list.pop(0)
print("count(3):", list.count(3))
print("get(2):", list.get(2))
list.printList()
