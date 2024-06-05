
print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")
print("="*30)

inkjet=[100,20]
laserjet=[200,50]
monye=200000
cmd =()
while cmd !="4":
    cmd = input("명령을 입력하세요: 1=사용, 2=상태, 3=보충, 4=종료>>")
    if cmd =="4":
        print("종료입니다.")
        break
    elif cmd =="2":
        print("잉크젯 상태 종이 %d 토너 %d" % (inkjet[0], inkjet[1]))  # 포맷 문자열 수정
        print("레이저젯 상태 종이 %d 토너 %d" % (laserjet[0], laserjet[1]))
        print("잔액 %d" %(monye))

    elif cmd =="1":
        printer=input("프린터를 선택하세요 1=잉크젯 2=레이저젯>>")
        if printer=="1":
            a = int(input("몇 장 프린트를 하겠습니까?"))
            inkjet[0]-=a
            b=a/10
            inkjet[1]-=b
        elif printer=="2":
            a=int(input("몇 장 프린트를 하겠습니까?"))
            laserjet[0]-=a
            b=a/10
            laserjet[1]-=b
    elif cmd =="3":
        choice =input("보충할 프린터를 선택하시오 1=잉크젯 2= 레이저젯>>")
        if choice=="1":
            paper=int(input("보충할 종이 수를 입력하세요>>"))
            toner=int(input("보충할 토너 수를 입력하세요>>"))
            inkjet[0]+=paper
            inkjet[1]+=toner
            monye-=(paper*100+toner*200)
        elif choice=="2":
            paper = int(input("보충할 종이 수를 입력하세요>>"))
            toner = int(input("보충할 토너 수를 입력하세요>>"))
            laserjet[0]+=paper
            laserjet[1]+=toner
            monye-=(paper*100+toner*200)

    else :
        print("잘못된 명령어 입니다.")
