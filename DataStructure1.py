import time

def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

n = 0
while True:
    start_time = time.time()
    result = recursive_fibonacci(n)
    end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time >= 300:  # 5분 이상
        print(f"재귀적 방법: n={n}, 수행시간: {elapsed_time:.2f} 초")
        break
    n += 1
