# config = utf-8 점프투파이썬 함수에 대해... 오늘 확실히 이해하자!!!!
def sum_function(a,b): # 1)입력값(인수)이 있는 함수.
    return (a+b+10-5)*15-100 # 마치 y = 2x + 3 처럼 쓸 수 있다
a = 3
b = 4
f = sum_function(a,b) #변수에 함수를 넣어버리면 변수가 함수역할을 한다
print(f)

print('------------')
def hi(): #2)입력값이 없는 함수
    return 'hi 이건 인수가 없이 그냥()로만 된 함수.'
f = hi()
print(f)
def multi(): #so why function with input value needed?
    return a*b+3
a = 9
b = 9
f = multi()
print(f,': 그런데 왜 인수가 필요한가? 그냥 리턴 수식만 작성해도 똑같지 않은가?')
print('-----------')

# 3) 결과값이 없는 함수도 있다. print 해서 문장 등으로 출력은 되어도... 함수를 return 했을 때 결과값이 없어 none...
def no_fun(a,b):
    print ('%d, %d is here, but this is no fucntion.' % (a, b))
print(no_fun(7,4)) # 7, 4 is here, but this is no fucntion. 는 출력이 되지만 곧이어 None이 아랫줄에 출력된다 논은 결과값 없음이란 뜻.
# 결과 값이 없음을 다시 한번 확인해 보자
f = no_fun(1,2)
print(f)

# 4) 입력값(인수)도 결과값도 없는 함수
def hi():
    print('hi')
print(hi())
print('------------')
# 5) 입력값이 여러개일 때 함수 * 요걸 붙인다
def args(*args):
    sum = 0
    for i in args:
        sum = sum+i
    return sum # 들여쓰기 주의 :: 이건 위의 for 문에 대한 리턴이니까.. 동일한 들여쓰기 단락에 써줘야 한다.
sum2 = args(1,2,3,4,5,6,7,8,9,10)
print(sum2)

