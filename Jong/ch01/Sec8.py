numbers = [11, 2, 63, 47, 50]

def find_min(numbers):
    return min(numbers)
def calculate_sum(numbers):
    return sum(numbers)


min_number = find_min(numbers)

# 합 구하기
sum_value = calculate_sum(numbers)

# 평균값 계산
average = sum_value / len(numbers)

# 결과 출력
print("최대값은", max(numbers), "최소값은", min_number, "합은", sum_value, "평균은", round(average, 1))