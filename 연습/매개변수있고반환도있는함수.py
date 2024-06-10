def abs(number):
    if number < 0:
        number = - number;
    return number


print('절대 값 : ',abs(-3))


def signGood(when):
    if when ==1:
        print("goodMornig")
    elif when == 2:
        print("dzd")
    else:
        print("ske")

signGood(1)