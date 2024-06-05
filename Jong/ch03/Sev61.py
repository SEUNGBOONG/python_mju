

b =[]
print("가계부 프로그램에 오신 것을 환영합니다. ")
print("="*60)

while True:
    a=input("명령을 입력하세요>> (1=내역입력, 2=결과 출력, 3=종료)")
    if (a == '1'):
        d=input("지출 항목을 입력하세요: ")
        c=int(input("지출 금액을 입력하세요: "))
        b.append((d,c))
    elif (a=='2'):
        total=0
        print("지출항목 리스트 입니다.")
        for d, c in b:
            print(f"{d},{c}원")
            total+=c
        print(f"지출 총액은 {total} 입니다. ")

    elif (a=='3'):
        print("프로그램을 종료합니다.")
        break
    else:
        print("잘못된 명령어 입니다. ")




