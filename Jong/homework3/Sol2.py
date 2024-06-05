def compute_score(**scores):
    if not scores:
        print("성적 정보가 없습니다.")
        return

    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    highest_score_student = max(scores, key=scores.get)
    lowest_score_student = min(scores, key=scores.get)

    print("[성적 산출 결과]")
    for student, score in scores.items():
        print(f"- {student}: {score}점")

    print(f"총점: {total_score}점")
    print(f"평균: {average_score:.1f}점")
    print(f"최고점자: {highest_score_student} ({scores[highest_score_student]}점)")
    print(f"최하점자: {lowest_score_student} ({scores[lowest_score_student]}점)")


def main():
    student_scores = {}

    while True:
        menu = input("메뉴: 1=입력 2=성적산출 q=종료 >> ")

        if menu == '1':
            while True:
                entry = input("성적을 입력하세요 (이름=점수): ")
                if entry == '.':
                    print("성적이 입력되었습니다.")
                    break
                try:
                    name, score = entry.split('=')
                    student_scores[name] = int(score)
                except ValueError:
                    print("잘못된 입력 형식입니다. '이름=점수' 형식으로 입력하세요.")

        elif menu == '2':
            compute_score(**student_scores)

        elif menu == 'q':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 메뉴 선택입니다. 다시 시도하세요.")


if __name__ == "__main__":
    main()
