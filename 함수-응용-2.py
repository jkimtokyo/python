# 인수에 True False
def truefalse(a=True):
    if a:
        print('I am a Man')
    else:
        print('Women')

print(truefalse()) # 출력값은 I am a Man, 아무 값도 없을 때는 위에서 설정한 초기값을 따른다.
print(truefalse(False)) # 출력값은 우먼
print(truefalse('a')) # Treu 출력값은 I am a Man
print(truefalse('b')) # True 출력값은 I am a Man

# 함수 내부에서 만든 (할당한) 변수는 함수 안에서만 통용된다.

a = 1
def afunction(a):
    return a+10
print(a) # 당연히 그냥 1이 출력값.
print(afunction(a)) # 11
print(afunction(10)) # 20

#------ 자료형의 참과 거짓 ----------

def truefalse(a):
    if a: # 그냥 이렇게 쓰면 a가 참일 때란 의미다.
        print('TRUE')
    else:
        print('..')

print(truefalse('')) # FALSE, 값이 비어있는 ''는 거짓이다.
print(truefalse('something')) # TRUE, 문자열 있음은 참이다
print(truefalse([])) # FALSE, 값이 비어있는 []는 거짓이다.
print(truefalse({})) # FALSE, 값이 비어있는 {}는 거짓이다.
print(truefalse(())) # FALSE, 값이 비어있는 ()는 거짓이다.
print(truefalse(1))  # TRUE, 1은 참이다.
print(truefalse(2))  # TRUE, 숫자 있음은 참이다,
print(truefalse(0))  # FALSE, 0은 거짓이다.
print(truefalse(None)) # FALSE, None은 거짓이다.
print(truefalse(True)) # TRUE
print(truefalse(False)) # FALSE

money = 0 # FALSE
if money:
    print('by TAXI')
else:
    print('by FOOT')

money = 1 # TRUE
if money:
    print('by TAXI')
else:
    print('by FOOT')
