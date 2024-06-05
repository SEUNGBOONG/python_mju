
num3= int("10")
print(num3)

a=input(print("첫번째 정수를 입력하세요:"))
b=input(print("두번쨰 정수를 입력하세요:"))
mu=input(print("덧셈인지 뺼셈인지 입력하세요: "))


if mu== "덧셈":
    print(int(a)+int(b),"+",int(a+b))

elif mu=="뺄셈":
    print(int(a-b))
else :
    print("잘못입력했습니다.")


