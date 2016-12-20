# if는 조건문인데 조건문이란 참과 거짓을 판단하는 것을 말한다.
# 비교연산자 작다, 크다, 같다, 같지 않다 !=, 크거나 같다 >=, 작거나 같다 <=
a = 3
b = 2
if b>a:
    print('something') # False, 아무것도 출력되지 않는다.
if a>b:
    print('True') # 출력값은 True

# 1,000엔 이상 돈 있으면 택시를 타라
money = 500
if money > 1000:
    print('TAXI')
else:
    print('by WALK') # by WALK

money = 1500
if money > 1000:
    print('by TAXI') # by TAXI
else:
    print('by WALK')

money = 1500
if money >= 1500:
    print('by TAXI') # by TAXI
else:
    print('by WALK')

# in, not in을 사용할 수 있다. 리스트, 문자열, 튜플에서
list = [1,2,3]
if 1 in list:
    print('TRUE') # TRUE
if 1 not in list:
    print('FALSE') # 이건 FALSE 라서 출력값이 안 나온다
if 4 not in list:
    print('TRUE') # TRUE

list = ('a','b','c') # 튜플에서도
if 'a' in list:
    print('True') # True

if 'j' in 'jkim': # True 문자열에서도
    print('True')

if 'h' not in 'jkim':
    print('True') # True

# 조건문의 참 거짓일 때 아무 일도 하지 않도록 설정하고 싶으면 pass
a = [1,2,3]
if 1 in a:
    pass
else:
    print('False') # TRUE이기 때문에 pass가 수행되고 아무런 값도 출력하지 않는다

a = [1,2,3]
if 4 not in a:
    pass
else:
    print('False') # TRUE이기 때문에 pass가 수행되고 아무런 값도 출력하지 않는다

# 다양한 조건 판단에 elif, 엘이프는 앞 조건이 거짓일 때만 발동한다. 갯수에 제한 없음.
money = 0
card = 1
if money:
    print('Taxi with cash')
elif card:
    print('Use your card')
else:
    print('WALK')
# 0 = FALSE, 1 = TRUE 따라서 출력값은 Use your card

if 'a' in 'abc': print('YES') # 한줄 콤마 뒤에 바로 써 주어도 된다.
if 'j' in 'jkim': pass
