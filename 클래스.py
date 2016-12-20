# 클래스는 일종의 함수이다. 그런데 전역함수라고나 할까...이전의 값을 기억하고 객체들이 그대로 상속을 받는... 특정 함수는 특정 기능 하나에 사용된다면 클래스는 하나의 로직을 클래스로 만들어 두고 변수에 값을 할당하듯 '객체'에 클래스 로직을 할당한다.

class Calcurator:
    def __init__(self):
        self.result = 0
    def adder(self,num):
        self.result += num
        return self.result

mycal1 = Calcurator() # mycal은 하나의 '객체'다, 그리고 mycal은 Calcurator'의 인스턴스'이다.
mycal2 = Calcurator()

print(mycal1.adder(1)) # 출력값은 1
print(mycal1.adder(2)) # 출력값은 3
print(mycal2.adder(3))
print(mycal2.adder(4)) # 출력값은 7 - 개별 객체는 개별 함수 역할을 수행할 수 있다. 동일한 기능이 복수로 필요할 경우에 객체만 간단히 생성하면 된다.

# 클래스 안의 변수가 변경되면 당연히 인스턴스들은 변경된 변수를 상속받는다.
class Serv:
    secret = 'FREE' # 클래스 안에 변수를 하나 생성

pay = Serv() # Serv 클래스의 인스턴스인 pay라는 객체를 생성
print(pay.secret) # 객체(.)클래스내변수를 호출하니 출력값 FREE를 얻을 수 있다. 이렇게 클래스에서 만들어 둔 변수나 함수는 인스턴스라면 모두 사용할 수 있다.

Serv.secret = 'Charge' # 클래스의 변수(원본에 해당하는)를 변경.
print(pay.secret) # 그대로 상속 받기에 출력값은 Charge

# 클래스 안에 함수 - 위 클래스에 더하기 기능을 추가한다. 클래스함수도 객체(.)클래스함수 구문으로 사용할 수 있다. 클래스함수는 다른말로 메쏘드라고 부른다.

class Serv:
    secret = 'PAID'
    def sum(self,a,b):
        return a+b
pay = Serv() # 여기서 다시 인스턴스를 정의하지 않으면 에러가 난다.

print(pay.secret,pay.sum(3,4)) # 출력값은 PAID 7
pay2 = Serv() # 물론 인스턴스는 얼마든지 만들어낼 수 있다.
print(pay2.secret,pay2.sum(1,2)) # PAID 3

# SELF 살펴보기, self는 객체가 클래스의 인스턴스인지 아닌지를 판단한다. def sum(self,a,b)에서 self 인수에 객체명이 들어오는 것이다. 그래서 원래라면 pay.sum(pay,1,2) 이렇게 써야하는데 자동적으로 인수가 전달되기 때문에 굳이 쓰지 않아도 되는 것이다.

# 객체변수

class Namebyun:
    classname = '클래스변수' # 클래스 변수임

oh = Namebyun() # 객체생성
oh.name = 'Jungsu' # 객체변수 생성. 객체변수란 '객체(.)변수명 = 값' 형태로 만들 수 있고 객체마다 고유한 객체변수를 저장한다. 위에서 본 클래스변수와 다르다. 클래스 변수는 인스턴스라면 모두 공유하는 변수지만 객체변수는 객체별.

kim = Namebyun() # 객체생성
kim.name = 'Jihoon'
print(oh.classname, oh.name,'and',kim.classname,kim.name) # 클래스변수 Jungsu and 클래스변수 Jihoon

oh.classname = 'NewCName'
print(oh.classname,'and',kim.classname) # NewCName and 클래스변수

class Newserv:
    def setname(self,name):
        self.newname = name
    def sum(self,a,b):
        result = a+b
        print('%s+%sは%sです。' %(a,b,result))

client = Newserv()
client.setname('キムジフン') # 인수값을 넣으면 다음 함수가 수행된다 self.newname = name / 여기서 self는 자동적으로 인수가 전달되므로 인수.newname = name 즉 client.newname = name이라는 변수가 할당됨.
print(client.newname) # キムジフン
print(client.sum(1,2)) # 1+2は3です。

# __init__ 란 무엇일까? f




