#/ Users / iseung - yeob / PycharmProjects / pythonProject / fibonacci1.py
#n=10, 결과: 100, 수행시간:6.9141387939453125e-06 초
#n=20, 결과: 400, 수행시간:1.71661376953125e-05 초
##n=100, 결과: 10000, 수행시간:0.0003807544708251953 초
#n=200, 결과: 40000, 수행시간:0.0015060901641845703 초
#n=1000, 결과: 1000000, 수행시간:0.037542104721069336 초
#이승엽  10/3
import time
def sample(A):
    n=len(A)
    sum=0
    for i in range(n):
        for j in range(n):
            sum+=A[i]*A[j]
    return sum

#데이터 크기에 따른 수행시간 확인

data_size =[10, 20, 100, 200, 1000]

for n in data_size:
    A =[1]*n
    start_time=time.time()
    result=sample(A)
    end_time = time.time()
    print(f"n={n}, 결과: {result}, 수행시간:{end_time - start_time:.5f} 초 ")

