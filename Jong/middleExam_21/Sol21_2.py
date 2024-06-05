print("가계부 프로그램을 실행합니다.")
print("=" * 30)

# 아이디와 비밀번호 확인
for _ in range(3):
    userId = input("아이디를 입력하세요:")
    if userId != '홍길동':
        print("아이디가 틀렸습니다. 다시 입력하세요.")
        continue
    userPassword = input('비밀번호를 입력하세요:')
    if userPassword != 'ABC':
        print("비밀번호가 틀렸습니다. 다시 입력하세요.")
        continue
    print(f"{userId}님 환영합니다.")
    break
else:
    print("3회 오류로 프로그램을 종료합니다.")
    exit()

# 가계부 리스트 초기화
my_list = []

while menu !="0" :
    menu = input("메뉴를 선택하세요 (1=출력, 2=입력, 3=삭제, 0=종료): ")

    if menu == "1":
        if not my_list:
            print("출력할 내용이 없습니다.")
        else:
            total_amount = sum(int(item.split()[1]) for item in my_list)
            print(", ".join(my_list), f"총액은 {total_amount} 원입니다.")
    elif menu == "2":
        item_money = input("새로운 항목과 가격을 입력하세요 (예: 점심 10000): ")
        my_list.append(item_money)

    elif menu == "3":
        del_item = input("삭제할 항목을 입력하세요: ")
        if del_item in my_list:
            my_list.remove(del_item)
            print(f"{del_item} 항목이 삭제되었습니다.")
        else:
            print("삭제할 항목이 없습니다.")

    elif menu == "0":
        break
    else:
        print("입력이 잘못되었습니다. 다시 입력해 주세요.")

print("가계부 프로그램을 종료합니다.")
