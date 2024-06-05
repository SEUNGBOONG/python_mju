
import time

def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return b

# 출력하고자 하는 피보나치 수열의 인덱스를 지정
n1 = 10
n2 = 20
n3 = 100
n4= 200
n5=100000
n6=1

# n1번째 피보나치 수 계산
start_time = time.time()
result1 = fibonacci(n1)
end_time = time.time()
elapsed_time1 = end_time - start_time

# n2번째 피보나치 수 계산
start_time = time.time()
result2 = fibonacci(n2)
end_time = time.time()
elapsed_time2 = end_time - start_time

print(f"{n1}번째 피보나치 수: {result1}, 수행시간: {elapsed_time1:.10f} 초")
print(f"{n2}번째 피보나치 수: {result2}, 수행시간: {elapsed_time2:.10f} 초")
print(f"{n3}번째 피보나치 수: {result2}, 수행시간: {elapsed_time2:.10f} 초")
print(f"{n4}번째 피보나치 수: {result2}, 수행시간: {elapsed_time2:.10f} 초")
print(f"{n5}번째 피보나치 수: {result2}, 수행시간: {elapsed_time2:.10f} 초")
print(f"{n6}번째 피보나치 수: {result2}, 수행시간: {elapsed_time2:.10f} 초")
