#python 출석확인과제
#60215276 이승엽 정보통신공학과

def hap(a, b):
    return a + b

def cha(a, b):
    return a - b

def hapcha(a, b, op):
    if op == '+':
        result = hap(a, b)
        print(f"두 수의 합을 구해 출력해주는 함수입니다 {a} {b}의 합은 {result}입니다")
    elif op == '-':
        result = cha(a, b)
        print(f"두 수의 차를 구해 출력해주는 함수입니다 {a} {b}의 차는 {result}입니다")
    else:
        print("정의되지 않은 연산입니다")

hapcha(10, 20, '+')
hapcha(10, 20, '-')
hapcha(-87, 172, '+')
hapcha(-87, 172, '-')
hapcha(10, 20, '*')  # 정의되지 않은 연산
