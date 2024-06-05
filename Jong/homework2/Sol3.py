coins = [['BTC', 50000], ['XRP', 20000], ['ADA', 30000]]

print("가상화폐 프로그램에 오신 것을 환영합니다")
while True:
    cmd = input("명령을 입력하세요 (1=입력, 2=내역확인, 3=삭제, q=종료) >> ")
    priceSum = 0
    if cmd == '1':
        while True:
            inputCmd = input("코인 정보를 입력하세요 (입력종료는 마침표) >> ")

            if inputCmd == '.':
                print()
                break
            else:
                inputCom, inputPrice = inputCmd.split()

            inputPrice = int(inputPrice)
            inputResult = [inputCom, inputPrice]

            for i in range(len(coins)):
                if coins[i][0] == inputCom:
                    coins[i][1] += inputPrice
                    break
                else:
                    coins.append(inputResult)
                    break

    elif cmd == '2':
        print("현재 보유중인 가상화폐 내역입니다")

        for i in range(len(coins)):
            print(coins[i][0], coins[i][1], '원', end=",")
            priceSum += coins[i][1]

        print("\n총 보유액은 %d 원입니다" % priceSum)
        print()

    elif cmd == '3':
        delete = input("삭제할 코인을 입력하세요 >> ")
        delete_exist = False

        for i in range(len(coins)):
            if coins[i][0] == delete:
                del coins[i]
                delete_exist = True
                print()
                break

        if not delete_exist:
            print("해당 코인이 없습니다")
            print()

    elif cmd == 'q':
        print("프로그램을 종료합니다")
        break

    else:
        print("다시 입력해주세요.")
        continue