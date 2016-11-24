# 입력값 인수가 복수개일 경우...
def many(*muji):
    sum = 0
    for i in muji:
        sum = sum+i
        return sum # 0, sum 바로 밑에서 리턴
v = many(0,1,2,3,4,5,6,7,8,9,10)
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
f = ifthen(1)
z = ifthen(2)
print(f,z) # One Two
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
print(textnum('sum',1,2,3,4,5),textnum('mul',1,2,3,4)) # 15 24

