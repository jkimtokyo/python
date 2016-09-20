# coding=utf-8

# 상속 - 위로부터 물려 받는 것.
class parent():
    def lastname(self):
        print("King")

class child(parent):
    def firstname(self):
        print("James")

james=child()
james.firstname()
james.lastname()

print('-----------------'+"\n")

# multi inheritance
class parent():
    def lastname(self):
        print("King")

class child():
    def firstname(self):
        print("James")

class Son(parent, child):
    def lastname(self):
        print('KIM') #상속 받았지만 아래에서 다시 데피니션 하면,재정의 한 것으로 써지는데 이것을 overriding

son2=Son()
son2.lastname()
son2.firstname()
print('----------------------'+'\n')

# 쓰레드 동시에 여러 프로세스가 돌게 하는 것 import threading
import threading

class Messenger(threading.Thread):
    def run(self):
        for _ in range(4):
            print(threading.currentThread().getName())
m=Messenger(name='message sending')
y=Messenger(name='receive message')
m.start() # 쓰레드는 run이 아닌 start
y.start()

print('\n')
# 램다 lambda 함수이름도 필요 없는 이름 없는 작은 함수, 한번만 간단하게 쓸 때.. 1회성
multi= lambda x: x+1 #def 함수 만들 필요없이 = lambda 변수: 식 형태임
print(multi(2))

# GitHub 레퍼지토리 쪽으로 이동시킴
