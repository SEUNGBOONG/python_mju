

i=0
menu_list=[]
monye=0
print("가계부 프로그램을 실행합니다.")
print("=" * 20)
while menu !="0":
    while i<=3:
        userId=input("아이디를 입력하세요:")
        if userId =="홍길동":
            userPasswrod=input("비밀번호를 입력하세요:")
            if userPasswrod =="123":
                print("홍길동님 환영합니다.")
            else:
                print("비밀번호가 틀렸습니다. 다시 입력하세요:")
                i+=1
                print("3회 오류로 프로그램을 종료합니다.")
                break
        else:
            print("아이디가 틀렸습니다. 다시입력하세요:")
            i+=1
            continue

    menu=input("메뉴를 선택하세요 1=출력 2=입력 3=삭제 0=종료:")
    if menu =="1":
        if menu_list==None:
            print("출력할 내용이 없습니다.")
        else:
            print(menu_list, monye,"원","총액은 ",monye,"입니다.")

    elif menu ==2:
        item=input("새로운 항목과 가격을 입력하세요:")
        item1=item[0:2]
        menu_list.append(item1)

        money1=int(item[3:])
        monye+=money1

    elif menu ==3:
        pop_list=input("삭제할 항목을 입력하세요:")







