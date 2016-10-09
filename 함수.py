# config = utf-8 점프투파이썬 함수에 대해... 오늘 확실히 이해하자!!!!

def sum_function(a,b): # 1) 입력값(인수)이 있는 함수. sum_function이란 이름의 함수고. 인수로 에이와 비라는 값을 받으며 결과값으로는 에이와 비를 더한 값을 출력해낸다.
    return a+b
a = 3
b = 4
f = sum_function(a,b) # 변수에 함수를 넣어버리면 변수가 함수역할을 한다
print(f)
# 2) 입력값이 없는 함수
def hi():
    return 'hi'
f = hi()
print(f)

def multi():
    return a*b
a = 9
b = 9
f = multi()
print(f)