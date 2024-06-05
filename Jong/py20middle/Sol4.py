

print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276")
print("="*30)
printer_list=[['잉크젯',200,100], ['레이저젯',200,100],['Epson',200,100]]
monye=200000

cmd=()
while cmd !="4":
    cmd = input("명령을 입력하세요 (1=사용 2=상태 3=보충 4=종료 >>")
    if cmd =="2":
        i=0
        for i in range(3):
            print("%s 종이 %d 토너 %d" % (printer_list[i][0], printer_list[i][1], printer_list[i][2]))
# print("%s 종이 %d 토너 %d" %(printer_list[1][0],printer_list[1][1],printer_list[1][2]))
            # print("%s 종이 %d 토너 %d" %(printer_list[2][0],printer_list[2][1],printer_list[2][2]))
        print("잔액은 %d" %monye)
    elif cmd =="1":
        printer=input("프린터와 장수를 입력하세요 (예: 잉크젯 20)>>")
        if printer[0:3]=="잉크젯":
            inkjet_paper=int(printer[4:])
            printer_list[0][1]-=inkjet_paper
            inkjet_toner = inkjet_paper/10
            printer_list[0][2]-=inkjet_toner
        elif printer[0:4]=="레이저젯":
            laserjet_paper=int(printer[5:])
            printer[1][1]-=laserjet_paper
            laserjet_toner =laserjet_paper/10
            printer_list[1][2]-=laserjet_toner
        elif printer[0:5]=="Epson":
            Epson_paper=int(printer[6:])
            printer_list[2][1]-=Epson_paper
            Epson_toner=Epson_paper/10
            printer_list[2][2]-=Epson_toner
        else:
            print("잘못 입력했습니다.")
    elif cmd =="3":
        printer=input("보충 프린터와 장수 토너수를 입력하세요: 예(잉크젯 100 500")
        if printer[0:3]=="잉크젯":
            inkjet_paper=int(printer[4:7])
            inkjet_toner=int(printer[8:10])
            monye-=(inkjet_toner*200+inkjet_paper*100)
        elif printer[0:4]=="레이저젯":
            laserjet_paper=int(printer[5:8])
            laserjet_toner=int(printer_list[9:11])
            monye-=(laserjet_paper*100+laserjet_toner*200)
        elif printer[0:5]=="Epson":
            Epson_paper=int(printer[6:9])
            Epson_toner=int(printer_list[10:12])
            monye-=(Epson_toner*200+Epson_paper*100)
        else:
            print("잘못 입력했습니다.")
    else:
        print("프로그램을 종료합니다.")

