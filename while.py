# config=utf-8
print('   ')
print("Welcome to While Quiz")
print('---------------')

guess=0 # 변수 초기화 해 주고...
while guess != 5: # 어차피 초기 변수가 0이니까..
    g=input('Guess the number : ')
    guess = int(g)
    if guess == 5:
        print("Good Answer!")
    else :
        print('Try Again....')
