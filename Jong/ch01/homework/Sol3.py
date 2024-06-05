#3. 문자열을 입력 받고, 모든 문자를 대문자로 변경하여 출력,
# 소문자로 변경하여 출력, 각 단 어의 첫문자만 대문자가
# 되도록 변경하여 출력하고, 마지막으로 변경된 문자열을
# 공백을 기준 으로 분리되도록 하여 그 결과로 생성된
# 리스트를 아래와 같이 출력하시오.


str = "you are the best artist"
print("문자열을 입력하세요: " +str)
print("대문자 출력: "+str.upper())
print("소문자 출력: "+ str.lower())
print("타이틀 출력: "+str.title())
split_str = str.title().split()

# 리스트 출력
print("리스트 출력:", split_str)