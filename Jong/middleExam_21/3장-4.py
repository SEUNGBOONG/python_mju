
print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276입니다.")
print("="*20)
my_memo = ['운동하기','영화 보기', '쇼핑하기']

while True:
    cmd=input("명령을 입력하세요>>")
    list = cmd.split(" ")
    if cmd =='종료':
        if cmd == '전체 출력':
            for n in cmd:
                print(n)
        elif list[0] == '메모' and list[2]=='추가':
            my_memo.append(cmd[6:])
            print(my_memo)
        elif list[0] =='메모' and list[2]=='보여줘':
            if list[1][-1] =='번':
                if list[1].isdigit():
                    number=int(list[1])
                    print(my_memo[number])
        elif list[0]=='메모' and list[2] =='삭제':
            if list[1][-1] =='번':
                if list[1].isdigit():
                    number2=int(list[1])
                    my_memo.remove(my_memo[number2])
                    print(my_memo)




    print("프로그램을 종료합니다.")
