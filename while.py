# config=utf-8
print('')
print("Welcome to While Quiz")
print('-----')

from random import randint
secret = randint(5,7)
guess = 6 # 변수의 초기화 ??

while guess != secret: # 어차피 초기 변수가 0이니까..
    g=input('Guess the number : ')
    guess = int(g)
    if guess == secret:
        print("Good Answer!")
    else :
        print('Try Again....')

print('')
print("Welcome to While Quiz")
print('-----')


guess = 6 # 변수의 초기화 ??

while guess != 6: # 어차피 초기 변수가 0이니까..
    g=input('Guess the number : ')
    guess = int(g)
    if guess == secret:
        print("Good Answer!")
    else :
        print('Try Again....')
