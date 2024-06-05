for i in range(2, 11):  # 2부터 10까지의 수
    print(f"{i}의 배수:", end=" ")
    for j in range(i, 101, i):  # i부터 100까지 i의 배수
        print(j, end=" ")
    print()  # 줄 바꿈
