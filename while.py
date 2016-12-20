# config=utf-8
# WHILE 문은 조건이 참이면 반복 되고, 거짓이 되는 순간 종료되는 반복문이다. WHILE 조건 :
num = 0
while num < 3: # 조건문 0부터 1,2까지
    num = num+1
    print('%d번 돌았습니다.' %num, end='') # 1번 돌았습니다.2번 돌았습니다.3번 돌았습니다.
print('')
print('-------------')

coffee = 1
while True: # WHILE 문의 조건문이 True 이므로 항상 참인 상태
    money = int(input('커피값은 100원입니다 : '))
    if money == 100:
        print('커피 나오셨습니다.')
        coffee = coffee - 1
    else: # 만약 100 입력이 아닐 경우에 출력되는 문장
        print('100원을 투입하여 주십시오')
    print('커피가 %d잔 남아 있습니다.' % coffee) # 100이 입력되면 -1잔이, 다른 숫자 입력되면 3잔 남았다고.. 그런데, 3잔을 다 마시고 또 100 입력하면 -1잔 남아있다고 출력된다.
    if not coffee:
        print('커피가 판매종료 되었습니다.')
        break

# WHILE 문을 강제로 종료 (빠져나가는) break
tea = 1
while True:
    money = int(input('아이스티는 120원입니다 : '))
    if money == 120:
        print('아이스티 나오셨습니다.')
        tea = tea-1
    else:
        print('120원을 투입하여 주세요.')
    print('아이스티는 %d잔 남았습니다.' % tea) # 여기서도 계속 100 투입하면 -1이 출력되는데...
    if not tea: # 이건 단순히 0일 때 아래 '모든 음료수가 판매 종료되었습니다'. 문장 출력을 위한 구문이며 여전히 120 넣으면 -1잔 출력된다.
        print('모든 음료수가 판매 종료되었습니다.')
        break # break 로 끊어야 비로서 더이상 반복되지 않고 종료된다.

# WHILE 구문에서도 CONTINUE 사용할 수 있다. 컨티뉴는 조건이 맞지 않으면 (무시하고) WHILE 구문 처음으로 돌아가는...
a = 0
while a < 10:
    a = a+1
    if a%2 ==1: continue # 2로 나눠 나머지가 1이니까 홀수고 홀수일 경우 무시하고 반복문을 a < 10:로 돌아가라.
    print(a) # 짝수들만 출력된다 2 4 6 8 10

# 무한루프
while True:
    print('무한루프') # 이건 계속 무한루프...