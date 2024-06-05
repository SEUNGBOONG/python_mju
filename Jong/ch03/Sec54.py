id_list=['홍길동','김영희','파이싼']

a=input("사용자 아이디를 입력하세요")


if a in id_list:
    print("등록된 사용자가 아닙니다.")
else:
    b, c = float(input("이수한 학점수와 평점을 입력하세요:")).split()
    if b > 140 and c > 4.0:
        print("우등졸업이 가능합니다.")
    elif b > 140 and 2.5 < c and c < 4.0:
        print("졸업이 가능합니다.")
    else:
        print("졸업이 불가능합니다.")

