
my_memo=['운동하기','영화 보기','쇼핑하기']

print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")

while str !="종료":
    print("=" * 20)
    str = input("명령을 입력하세요 >> ")
    if str =='전체 출력':
        for i in my_memo:
            print(i)
    elif str[0:5]=="메모 추가":
        input_memo=str[6:]
        my_memo.append(input_memo)
        print(my_memo)
    elif str[0:2]=="메모" and str[6:9]=="보여줘":
        see=int(str[3])
        print(my_memo[see])
    elif str[0:2]=="메모" and str[6:8]=="삭제":
        pop=int(str[3])
        my_memo.pop(pop)

    elif str =="종료":
        print("프로그램을 종료합니다.")
    else:
        print("다시 입력하세요")


