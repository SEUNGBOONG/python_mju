print("가계부 프로그램에 오신것을 환영 합니다. ")
print("=" * 45)
print()

ins = input('명령을 입력하세요 (1= 내역 입력, 2= 결과 출력, 3=종료)')
monye_list = []
price_list = []
total = 0

while ins != '3':
    if ins == '1':
        monye1 = input("지출항목을 입력하세요: ")
        price1 = int(input("지출 금액을 입력하세요: "))
        monye_list.append(monye1)
        price_list.append(price1)
        total += price1
    elif ins == '2':
        print('지출 항목 리스트입니다.')
        print(monye_list)
        print(price_list)
        print('지출 총액은', total, '원입니다.')
    else:
        print('잘못된 명령입니다.')
    print()
    ins = input('명령을 입력하세요 (1= 내역 입력, 2= 결과 출력, 3=종료)')
print('프로그램을 종료합니다. ')
