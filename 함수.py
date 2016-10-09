# config = utf-8 점프투파이썬 함수에 대해... 오늘 확실히 이해하자!!!!
def sum_function(a,b): # 1) 입력값(인수)이 있는 함수. sum_function이란 이름의 함수고. 인수로 에이와 비라는 값을 받으며 결과값으로는 에이와 비를 더한 값을 출력해낸다.
    return a+b+10-5
a = 3
b = 4
f = sum_function(a,b) # 변수에 함수를 넣어버리면 변수가 함수역할을 한다
print(f)
print('------------')

def hi(): # 2) 입력값이 없는 함수
    return 'hi'
f = hi()
print(f)

def multi():
    return a*b+3
a = 9
b = 9
f = multi()
print(f) # so why function with input value needed?
print('-----------')

# 3) 결과값이 없는 함수도 있다. print 해서 문장 등으로 출력은 되어도... 함수를 return 했을 때 결과값이 없어 none...
def no_fun(a,b):
    print('%d, %d is here, but this is no fucntion.' % (a, b))
print(no_fun(7,4)) # 7, 4 is here, but this is no fucntion. 는 출력이 되지만 곧이어 None이 아랫줄에 출력된다 논은 결과값 없음이란 뜻. 
