def cmd_input():
    return input("명령을 입력하세요 (1=사용 2=상태 3=보충 4=등록 5=삭제 q=종료) >> ")


def printer_use(printer_dict, name, page):
    if name in printer_dict:
        printer_dict[name][0] -= page
        printer_dict[name][1] -= page // 10
    else:
        print(f"프린터 {name}가 존재하지 않습니다.")
    return printer_dict


def printer_status(printer_dict, budget):
    for name, (pages, toner) in printer_dict.items():
        print(f"{name} 종이 {pages} 토너 {toner}")
    print(f"예산 {budget}원")


def printer_refill(printer_dict, budget, name, page, toner):
    if name in printer_dict:
        cost = page * 100 + toner * 200
        if budget >= cost:
            printer_dict[name][0] += page
            printer_dict[name][1] += toner
            budget -= cost
        else:
            print("예산이 부족합니다.")
    else:
        print(f"프린터 {name}가 존재하지 않습니다.")
    return printer_dict, budget


def printer_add(printer_dict, name, page, toner):
    if name not in printer_dict:
        printer_dict[name] = [page, toner]
    else:
        print(f"프린터 {name}가 이미 존재합니다.")
    return printer_dict


def printer_del(printer_dict, name):
    if name in printer_dict:
        del printer_dict[name]
        print(f"삭제 후 남아 있는 프린터들: {list(printer_dict.keys())}")
    else:
        print(f"프린터 {name}가 존재하지 않습니다.")
    return printer_dict


def main():
    printer_dict = {
        '잉크젯': [200, 100],
        '레이저젯': [200, 100],
        'Epson': [200, 100]
    }

    budget = 200000

    while True:
        cmd = cmd_input()

        if cmd == '1':
            name, page = input("프린터와 장수를 입력하세요 (예: 잉크젯 20) >> ").split()
            page = int(page)
            printer_dict = printer_use(printer_dict, name, page)

        elif cmd == '2':
            printer_status(printer_dict, budget)

        elif cmd == '3':
            name, page, toner = input("프린터와 장수 및 토너를 입력하세요 (예: 잉크젯 100 50) >> ").split()
            page = int(page)
            toner = int(toner)
            printer_dict, budget = printer_refill(printer_dict, budget, name, page, toner)

        elif cmd == '4':
            name, page, toner = input("등록할 프린터와 장수 및 토너를 입력하세요 (예: 잉크젯 100 50) >> ").split()
            page = int(page)
            toner = int(toner)
            printer_dict = printer_add(printer_dict, name, page, toner)

        elif cmd == '5':
            name = input("삭제할 프린터를 입력하세요 (예: 잉크젯) >> ")
            printer_dict = printer_del(printer_dict, name)

        elif cmd == 'q':
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 명령입니다. 다시 입력해주세요.")


if __name__ == "__main__":
    main()
