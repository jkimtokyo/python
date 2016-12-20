# 입력값 인수가 복수개일 경우...
def many(*moji):
    sum = 0
    for i in moji:
        sum = sum+i
    return sum # 0, sum 바로 밑에서 리턴
v = many('a','b') # TypeError: for +: 'int' and 'str'
print(v)

def many(*muji):
    sum = 0
    for i in muji:
        sum = sum+i
    return sum # 55, for 전체를 리턴
v = many(0,1,2,3,4,5,6,7,8,9,10)
print(v)

# 인수 가지고 if 만들어 보기
def ifthen(a):
    if a == 1:
        val = 'One'
    elif a == 2:
        val = 'Two'
    elif a == 3:
        val = 'Three'
    return val
print(ifthen(1),ifthen(2),ifthen(3)) # One Two Three

# 인수 하나는 텍스트 하나는 숫자로 if 만들기
def textnum(a,*b):
    if a == 'sum':
        v = 0
        for i in b:
            v = v+i
    elif a == 'mul':
        v = 1
        for i in b:
            v = v*i
    return v
print(textnum('sum',1,2,3,4),textnum('mul',1,2,3,4)) # 10 24

# 리턴을 콤마로 여러개 식을 넣어버릴 경우, 리턴 수식엔 a,b,c 모두 없어도 되지만 활용문 (summul(n1,n2,n3)에선 3자리수 맞춰야 함
def summul(a,b,c):
    return a+b+c, a*b*c, c-a
print(summul(1,2,4)) # 7, 8, 3

# 7,8,3 을 각각 출력값으로 받으려면 -
t,g,f = summul(1,2,4) # 변수를 콤마로 자리 수 3개 맞춰서 각각 출력하면 된다
print(t) # 7
print(g) # 8
print(t-g)

# * return을 두줄로 써도 한 줄의 리턴만 먹는다, return문을 만나는 순간 결과값을 돌려주고 함수를 빠져나온다. *
def summul(a,b,c):
    return a+b+c
    return a*b
print(summul(1,2,3)) # 출력값은 6만 나온다

# 리턴으로 함수 끝내기 (빠져나오기)
def exit(nick):
    if nick == 'me':
        return
print(exit('me')) # 인수로 me가 들어오면 함수를 종료한다