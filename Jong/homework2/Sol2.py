list_b = [55, 35, 40, 70, 65, 30]
count = 0
testAvg = sum(list_b) / 6

for i in range(len(list_b)):
    if list_b[i] < 40:
        count += 1

print("40점 미만 과목수 :", count)
print("평균 점수:", testAvg)
if count == 0 and testAvg >= 60:
    print("축하합니다. 합격하셨습니다.")
else:
    print("아쉽습니다. 불합격하셨습니다.")

