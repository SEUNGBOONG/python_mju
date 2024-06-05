

print("메모앱에 오신 것을 환영합니다. ")
my_memo = ['운동하기', '헬스 가기', '마트 가기']

while str !="종료":
    print("명령을 입력하세요:")
    str = input(">>")
    print("=" * 20)

    if str =='전체 출력':
        for i in my_memo:
            print(i)


    elif str[0:2]=='메모' and str[3:5]=='추가':
        new_memo=str[6:].strip()
        my_memo.append(new_memo)
        print(my_memo)


    elif str[0:2]=='메모' and str[6:10]=='보여줘':
        if str[3].isdigit():
            number=int(str[3])
            print(my_memo[number])
        else:
            print("리스트에 없습니다.")


    elif str[0:2]=='메모' and str[6:9]=='삭제':
        if str[3].isdigit():
            number2=int(str[3])
            my_memo.pop(number2)
            print(my_memo)
        else:
            print("삭제할게 없습니다.")
    elif str=="종료":
        break
    else:
        print("없는 명령어 입니다.")