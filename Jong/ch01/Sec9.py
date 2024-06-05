


# 사용자 입력 받기
name = input("이름을 입력하세요: ")
age = input("나이를 입력하세요: ")
student_id = input("학번을 입력하세요: ")

# 결과 출력
print("이름", name, "나이", age, "세", "학번", student_id, "입니다")

# 사용자 입력 받기
inputs = input("이름과 나이와 학번을 입력하세요: ")

# 입력 문자열을 공백을 기준으로 분리
name, age, student_id = inputs.split()

# 결과 출력
print("이름", name, "나이", age, "세", "학번", student_id, "입니다")
