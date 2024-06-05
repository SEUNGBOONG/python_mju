my_memo=['운동하기','헬스 가기','마트 가기']
print("메모 앱에 오신 것을 환영합니다. ")

while str !='종료':
    print("="*20)
    str=input("명령을 입력하세요.\n >>")
    if str[0:5]=="메모 추가":
        result=str[6:]
        my_memo.append(result)
        print(my_memo)
    elif str == '전체 출력':
        for i in my_memo:
            print(i)

    elif str[0:2]=="메모" and str[6:9]=='보여줘' :
        num1=int(str[3])
        print(my_memo[num1])

    elif str[0:2]=="메모" and str[6:]=="삭제":
        num2 = int(str[3])
        my_memo.pop(num2)
        print(my_memo)




