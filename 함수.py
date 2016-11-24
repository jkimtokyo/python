def sum(a,b): # 1.입력값(인수)있고 출력값(리턴값)도 있고
    return a+b # 여기서 리턴 가로줄 없으면 none이 출력된다 즉 출력값이 없는 함수가 된다.

c = sum(3,4)
print(c) # 7

a = 2
b = 2
z = sum(a,b)
print(z) # 3

def gop(a):
    r = a*'Fuck '*2
    return r
print(gop(a)) # Fuck Fuck

def r(b):
    return b+10
print(r(b)) # 12

# 2.입력값 없고, 출력값은 있고 - return 출력식만 정의해 둘 때-
def noinput():
    return '18 FUCK'
print(noinput()) # 18 Fuck
f = noinput()
print(f) # 18 FUCK

# 3.입력값(인수)있고 출력값 없는 함수
def non(a,b):
    print('%d과 %d' %(a,b)) # 2와 2로 프린트 된다.
r = non(3,4)
print(r) # None = 출력값 없는 함수

# 4.입력값도 없고 출력값도 없는 함수
def non2():
    print('just hi')
r = non2()
print(r) # 입력값도 없고 출력값도 없다. None

