print("가계부 프로그램을 실행합니다.")
print("="*50)
menu_list=[]
money=0
while True:
    name = input("아이디를 입력하세요: ")
    if name!="홍길동":
        print("잘못 입력했습니다.")
        continue
    elif name == "홍길동":
        password=input("비밀번호를 입력하세요:")
        if password !="ABC":
            password=input("비밀 번호가 틀렸습니다. 다시 입력하세요:")
            continue
        elif password=="ABC":
            print("홍길동님 환영합니다.")
            break
    else:
        print("3회 오류로 종료합니다.")
        break


menu=""
while menu != "0":
    menu=input("메뉴를 선택하세요 1=출력 2=입력 3=삭제 0=종료: ")
    if menu=="1":
        if not menu_list:
            print("출력할 내용이 없습니다.")
        else:
            for i in menu_list:
                print(i)
            print("총액은 %d원 입니다." %money)
    elif menu =="2":
        item=input("새로운 항목과 가격을 입력하세요:")
        menu_list.append(item)
        money+=int(item.split()[1])
    elif menu=="3":
        pop=input("삭제할 항목과 가격을 입력하세요")
        if pop in menu_list:
            menu_list.pop(pop)
            money-=int(item.split()[1])
    elif menu == "0" :
        print("가계부 프로그램을 종료합니다.")
        break
    else :
        print("잘못입력했습니다.")











