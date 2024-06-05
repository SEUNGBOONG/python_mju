class Robot:
    name = "휴보"
    weight = 45

    def speak(self):
        print("안녕하세요 휴보입니다.")

    def move(self):
        print("휴보가 이동합니다.")


robot1 = Robot()
robot2 = Robot()

robot2.move()
robot1.speak()