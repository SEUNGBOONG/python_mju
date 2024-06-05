
print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")
print("="*60)

my_memo = ['운동하기','영화 보기','쇼핑하기']

while True:
    cmd=input("명령을 입력하세요>> ")
    if cmd =='전체 출력':
        for memo in my_memo:
           print(memo)
        print("="*60)
    elif cmd =='메모 추가':
        a= input()
        my_memo.append(a)
        print(my_memo)
        print("="*60)
    elif cmd =='메모 3번 보여줘':
        print(my_memo[3])
        print("="*60)
    elif cmd =='메모 2번 삭제':
        del my_memo[1]
        print(my_memo)
        print("="*60)
    elif cmd =='종료':
        print("프로그램을 종료합니다. ")
        print("="*60)
        break

