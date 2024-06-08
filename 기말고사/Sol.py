member = {123456:["abc123", "홍길동", 100000, "6/27 13:00"]}

def login():
    id = int(input("회원번호를 입력하세요"))
    pw = input("비밀번호를 입력하세요")
    if (id in member.keys() and member[id][0] == pw):
        print(member[id][1], "회원님 반갑습니다.")
        return id
    else:
        print("로그인에 실패했습니다")
        return 0

def register():
    name = input("성함을 입력해 주세요")
    id = int(input("회원번호를 입력해주세요"))
    pw = input("비밀번호를 입력해주세요")
    member[id] = [pw, name, 0, "None"]
    print(member[id][1], "회원님 반갑습니다.")
    return id

def schedule(my_id):
    print("다음 일정은", member[my_id][3], "입니다")
    cmd = input("변경을 원하십니까? (1=일정변경 0=일정유지)")
    if (cmd == '1'):
        order = input("원하시는 일정을 입력해 주세요")
        member[my_id][3] = order
        print("다음 일정이", member[my_id][3],"으로 변경되었습니다.")

def payment(my_id):
    result = 200000 - member[my_id][2]
    print("회비가", result, "원 부족합니다")
    cmd = int(input("얼마를 지불하시겠습니까?"))
    result -= cmd
    print("남은 회비 잔액은", result, "원입니다.")

