

money_list =[]
price_list=[]

print("가계부 프로그램에 오신 것을 환영합니다.")
print("="*60)

cmd = input("명령을 입력하세요: 1=내역입력, 2=결과 출력 3= 종료")
if cmd == 1:
    item=input("지출항목을 입력하세요:")
    price_list.append(item)
    money= input("지출 금액을 입력하세요:")
    money_list.append(money)

elif cmd == 2:
    print("지출항목 리스트 입니다.")
    print(price_list)
    print(money_list)