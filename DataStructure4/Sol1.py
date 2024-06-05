def bublle_sort(arr):
    n = len(arr)
    comparisons =0
    swaps=0
    for i in range(n):
        #마지막 i개의 원소는 이미 정렬되어 있으므로 제외

        for j in range (0, n-i-1):
            comparisons +=1

            if arr[j] >arr[j+1]:
                #순서가 잘못되면 자리를 바꾼다.
                arr[j], arr[j+1]=arr[j+1], arr[j]
                swaps +=1
    return comparisons, swaps
size =100
unsorted_list =list(range(size, 0 , -1))#역순으로 정렬된 리스트
#정렬하기 전의 비교와 자리 바꿈횟수
comparisons_before, swaps_before =bublle_sort(unsorted_list.copy())
unsorted_list =list(range(1,size+1)) #이미 정렬된 리스트
#정렬하기 전 비교와 자리 바꾸기 횟수
comparisons_after, swaps_after =bublle_sort(unsorted_list.copy())
print(f"정렬 전 (역순): 비교 {comparisons_before}회, 자리 바꿈 {swaps_before}회")
print(f"정렬 전 (정렬된상태): 비교 {comparisons_after}회, 자리 바꿈 {swaps_after}회")

#각 비교와 자리바꿈이 상수시간이라고 가정하면 다음과 같다.
##1. 비교에 걸리는 시간:
#- 정렬 전(역순): c1 *N^2
##- 정렬 전(정렬된 상태): c2*N
#2. 자리 바꿈에 걸리는 시간:
#-정렬 전(역순): c3 *N^2
#-정렬 전(정렬된 상태): 0

