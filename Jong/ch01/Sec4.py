#1. 내 나이는 20 살 이라고 출력하는데 20은 숫자로 나머지는 문자열로 print문에 입력 2. 한줄 공백 출력
#3. year 에 2023 저장
#4. month, date, day 에 3과 1과 “수” 를 한 줄로 저장
#5. date1, date2 에 3와 5를 한 줄로 저장
#6. date 에 date1과 date2의 합을 저장
#7. day 에 문자열 수요일을 저장
#8. 오늘 날짜는 2023 년 3 월 8 일 수 요일 입니다 라고 출력



age = 20
print(str(age))

year = 2023

month = 3
date = 1
day = "수"
date1 = 3
date2 = 5
date = date1 + date2

# day 변수를 "wed"로 바꾸는 부분은 삭제합니다.

print("오늘 날짜는 " + str(year) + "년 " + str(month) + "월 " + str(date) + "일 " + day + "요일 입니다.")
