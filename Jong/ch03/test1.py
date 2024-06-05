# 초기 메모 리스트 정의
my_memo = ['운동하기', '영화 보기', '쇼핑하기']

# 시작 메시지 출력
print('파이썬 중간고사 제 이름은 이승엽 학번은 60215276 입니다.')

# 무한 루프 시작
while True:
    # '*' 문자 20번 반복하여 출력
    print('*' * 20)
    # 사용자에게 명령 입력 요청
    print("명령을 입력하세요>>")
    # 사용자 입력 받기
    cmd = input()
    # 사용자 입력을 공백을 기준으로 분할하여 리스트로 만들기
    c_list = cmd.split(' ')

    # 사용자가 '종료'를 입력하면 루프를 종료
    if cmd == '종료':
        print('프로그램을 종료합니다.')
        break

    # 사용자가 '전체 출력'을 입력하면 메모 리스트의 모든 항목을 출력
    elif cmd == '전체 출력':
        for n in my_memo:
            print(n)

    # 사용자가 '메모 추가 XXXX'와 같이 입력하면 메모를 리스트에 추가
    elif c_list[:2] == ['메모', '추가']:
        my_memo.append(cmd[6:])
        print(my_memo)

    # 사용자가 '메모 X번 보여줘'와 같이 입력하면 X번째 메모를 출력
    elif c_list[0] == '메모' and c_list[2] == '보여줘' and c_list[1][-1] == '번':
        if c_list[1][:-1].isdigit():  # 숫자인지 검사하는것 isdigit
            num = int(c_list[1][:-1])  # 숫자 부분 추출
            print(my_memo[num])

    # 사용자가 '메모 X번 삭제'와 같이 입력하면 X번째 메모를 삭제
    elif c_list[0] == '메모' and c_list[2] == '삭제' and c_list[1][-1] == '번':
        if c_list[1][:-1].isdigit():
            num = int(c_list[1][:-1])  # 숫자 부분 추출 후 형변환
            my_memo.remove(my_memo[num])  # 해당 메모 삭제
            print(my_memo)
