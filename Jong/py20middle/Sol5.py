

my_memo=["운동하기","영화 보기", "쇼핑하기"]

print(" 파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")


cmd=()
while cmd !="종료":
    print("="*20)
    cmd = input("명령을 입력하세요>>")
    if cmd =="전체 출력":
        for i in my_memo:
            print(i)
    elif cmd[0:2]=="메모" and cmd[3:5]=="추가":
        new_memo=cmd[6:]
        my_memo.append(new_memo)
        print(my_memo)
    elif cmd[0:2]=="메모" and cmd[6:9]=="보여줘":
        if cmd[3].isdigit():
            a=int(cmd[3])
            print(my_memo[a])
        else: print("잘못 입력했습니다")
    elif cmd[0:2]=="메모" and cmd[6:8]=="삭제":
        if cmd[3].isdigit():
            a=int(cmd[3])
            my_memo.pop(a)
            print(my_memo)
    elif cmd=="종료":
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못 입력했습니다.")
