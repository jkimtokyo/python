#config=utf-8

print('Welcome!')
g=input('Input means Get input vlaue from User: ')
guess=int(g)
if guess==5:
    print('You Win!')
else:
    print('You Lose!')
print('----------------')

# 분기를 위해서는 들여쓰기
print('Welcome!')
g=input('Input input vlaue second chance: ')
guess=int(g)
if guess==5:
    print('You Win!')
else:
    if guess>5:
        print('Sorry, Little bit High')
    else:
        print('Sorry, Little bit Low')

# 자 이제 반복. 정답 맞출 때까지... While


