while(True):
    order = input("1=섭씨->화씨, 2=화씨->섭씨, q=종료")

    if(order == "1"):
        c = float(input("섭씨 온도를 입력하세요: "))
        f = float((c * 9 / 5) + 32)
        c = format(c, '.2f')
        f = format(f, '.2f')
        print("{0}도는 화씨로 {1}도입니다.".format(c, f))
    elif(order == "2"):
        f = float(input("화씨 온도를 입력하세요: "))
        c = float((f - 32) * 5 / 9)
        c = format(c, '.2f')
        f = format(f, '.2f')
        print("{0}도는 섭씨로 {1}도입니다.".format(f, c))
    elif(order == "q"):
        print("프로그램을 종료합니다.")
        break
    print()