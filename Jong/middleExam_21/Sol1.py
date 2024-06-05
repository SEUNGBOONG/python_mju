from Jong.pythonmiddle.Sol3 import init_money

inkjet=[100,20]
laserjet=[200,50]
init_monye=200000


print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")
print("="*60)

ch=""
while ch !="4":

    ch = input("명령을 입력하세요: (1=사용 2=상태 3=보충 4=종료)")

    if ch =="1":
        printer=input("프린터를 선택하세요 1=잉크젯 2=레이저젯")

        if printer =="1":
            a=int(input("몇장 프린트하겠습니까?"))
            inkjet[0]-=a
            inkjet[1]-= int(a/10)

        else:
            b=int(input("몇 장 프린트하겠습니까?"))
            laserjet[0]-=b
            laserjet[1]-=int(b/10)

    elif ch =="2":
        print("잉크젯 상태종이:",inkjet[0],"토너:",inkjet[1])
        print("레이저젯 상태종이:",laserjet[0],"토너:",laserjet[1])
        print("잔액",init_money,"원")

    elif ch =="3":
        printer=input("보충할 프린터를 선택하세요 1=잉크젯 2=레이저젯")
        if printer == "1":
            paper=int(input("종이수를 입력하세요:"))
            toner=int(input("토너수를 입력하세요:"))
            init_monye-=(paper*100) +(toner*200)
            inkjet[0]+=paper
            inkjet[1]+=toner

        elif printer =="2":
            paper = int(input("종이수를 입력하세요:"))
            toner = int(input("토너수를 입력하세요:"))
            init_monye-=(paper*100)+(toner*200)
            laserjet[0]+=paper
            laserjet[1]+=toner
            print("잔액",init_monye,"원 입니다.")

    elif ch =="4":
        print("프로그램을 종료합니다.")

    else:
        print("잘못된 명령어 입니다.")




