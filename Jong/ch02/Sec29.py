
animals =['개','고양이', '토끼', '다람쥐','거북이']
numbers = [0,1,2,3,4,5]


print("거북이와 토끼의 위치\n",animals.index("토끼"))
print(animals.index("거북이"))
animals.append("원숭이")
animals.insert(3,"펭귄")
print(animals)
numbers.extend([6,7,8])
print(numbers)

