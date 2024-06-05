list_a = []
for i in range(1,101):
    if i % 3 == 0 and i % 7 == 0:
        list_a.append(i)
        print("3과 7의 공배수 :", i)

print("3과 7의 최소공배수 :", min(list_a))
