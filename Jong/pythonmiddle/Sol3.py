inkjet=[100,20]
laserjet=[200,50]
init_money=200000

print("파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.")
print("="*40)


while str !="4":
    str =input("명령을 입력하세요:(1=사용 2=상태 3=보충 4=종료)>>")
    if str=="2":
        print("잉크젯 상태 종이 %d 토너 %d"%(inkjet[0],inkjet[1]))
        print("레이저젯 상태 종이 %d 토너 %d" %(laserjet[0],laserjet[1]))
        print("잔액 %d 원"%init_money)


    elif str =="1":


        printer =input("프린터를 선택하세요:(1=잉크젯 2=레이저젯)>>")
        if printer=="1":
            inkjet_paper=int(input("몇 장 프린트하겠습니까?>>"))
            inkjet[0]-=inkjet_paper
            inkjet[1]-=(inkjet_paper/10)
        elif printer =="2":
            laserjet_paper=int(input("몇 장 프린트하겠습니까?>>"))
            laserjet[0]-=laserjet_paper
            laserjet[1]-=(laserjet_paper/10)



    elif str =="3":
        printer=input("보충하실 프린터를 선택하세여: (1=잉크젯 2=레이저젯)>>")
        if printer=="1":
            paper=input("종이 수를 입력하세요>> ")
            toner=input("토너 수를 입력하세요>> " )

            inkjet_paper=int(paper)
            inkjet_toner=int(toner)

            init_money-= (inkjet_paper*100)
            init_money-= (inkjet_toner*200)



            inkjet[0]+=inkjet_paper
            inkjet[1]+=inkjet_toner



        elif printer=="2":
            paper = input("종이 수를 입력하세요>> ")
            toner = input("토너 수를 입력하세요>> ")

            laserjet_paper = int(paper)
            laserjet_toner = int(toner)

            init_money -= (laserjet_paper * 100)
            init_money -= (laserjet_toner * 200)

            laserjet[0] +=laserjet_paper
            laserjet[1] +=laserjet_toner

    else:
        print("잘못된 명령어 입니다. ")




