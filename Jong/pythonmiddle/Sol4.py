

printer_list=[['잉크젯',200,100],['레이저젯',200,100],['Epson',200,100]]
money=200000
print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")
print("="*50)
while str !="4":
    str = input("명령을 입력하세요:(1=사용 2=상태 3=보충 4=종료) >> ")
    if str == "1":
        printer=input("프린터와 장수를 입력하세요 (예: 잉크젯 20) >>")
        if printer[0:3] ==printer_list[0][0]:
            use_paper = int(printer[4:])
            printer_list[0][1] -= use_paper
            printer_list[0][2] -= (use_paper/10)
        elif printer[0:4]==printer_list[1][0]:
            use_paper =int(printer[5:])
            printer_list[1][1] -=use_paper
            printer_list[1][2] -=(use_paper/10)
        elif printer[0:5]==printer_list[2][0]:
            use_paper =int(printer[6:])
            printer_list[2][1] -=use_paper
            printer_list[2][2] -=(use_paper/10)

    elif str == "3":
        printer=input("보충 프린터와 장수와 토너수를 입력하세요: (예: 잉크젯 100 500) >>")
        if printer[0:3]==printer_list[0][0]:
            full_paper= int(printer[4:7])
            full_toner = int (printer[8:])
            printer_list[0][1]+=full_paper
            printer_list[0][2]+=full_toner
            money-=(full_paper*100+full_toner*200)
        elif printer[0:4]==printer_list[1][0]:
            full_paper= int(printer[5:8])
            full_toner = int (printer[9:])
            printer_list[1][1]+=full_paper
            printer_list[1][2]+=full_toner
        elif printer[0:5]==printer_list[2][0]:
            full_paper= int(printer[6:9])
            full_toner = int (printer[10:])
            printer_list[2][1]+=full_paper
            printer_list[2][2]+=full_toner
    elif str=="2":
        for i in range(3):
            print(printer_list[i][0],"종이",printer_list[i][1],"토너",printer_list[i][2])
        print("잔액 %d" %money)
    elif str =="4":
        print("프로그램을 종료합니다.")

