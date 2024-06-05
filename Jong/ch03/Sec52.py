# 1. 두 개의 정수를 입력하여 num1과 num2에 저장함. int() 함수로 문자열을 정수로 변환함.
# 예: int(“10”) 은 정수 10을 반환함.
# 2. 원하는 연산이 덧셈인지 뺄셈인지 질문함.
# 3. 덧셈도 뺄셈도 아닌 것을 입력하면 입력이 잘못되었다고 답변함.
# 4. 연산 조건에 따라 두 수를 계산하여 결과를 아래와 같이 출력함. (세 번 실행한 결과임)

num1 = int(input("첫 번째 정수를 입력하세요: "))
num2 = int(input("두 번째 정수를 입력하세요: "))

operation = input("덧셈 또는 뺄셈을 선택하세요 (+ 또는 -): ")

if operation == '+':
    result = num1 + num2
    print("두 수의 합은", result, "입니다.")
elif operation == '-':
    result = num1 - num2
    print("두 수의 차는", result, "입니다.")
else:
    print("입력이 잘못되었습니다. 덧셈 또는 뺄셈을 선택하세요.")
