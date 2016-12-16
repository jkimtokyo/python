# 파일을 새로 만들어 보고 프로그램을 통해 파일을 써보고 파일에 쓴 내용을 읽어보는 프로그램 만들어 보기
# open('파일명.확장자','읽기r 쓰기w 추가a') f = open('doc.txt','r') - w r a 도 따옴표로 감싸야 함.
# 파일 쓰기모드 w로 하면 이미 파일명이 존재할 경우 원래 있던 내용 없어지고, 파일이 없으면 새로운 파일이 생성된다. 쓸 때는 .write()

f = open('/Users/JKim/Desktop/source/new.txt','w') # 내 맥 바탕화면/source 경로에다가 new.txt 파일 생성됨, 여러번 RUN 해도 중복 파일 생기진 않는다.
f.write('What do I write something in here?')
f.close() #파이참 종료 시 파일객체도 종료되어 안써줘도 되나 쓰기 모드로 열었던 파일을 닫지 않고 사용하려 할 때 오류가 발생되니까 반드시 써주는 것이 좋다.

g = open('/Users/JKim/Desktop/source/g.txt','w')
for i in range(1,4):
    data = 'Number is %d. \n' %i #  \n은 한줄 내려쓰기. Number is 1. (줄 바꿈) Number is 2.
    g.write(data)
g.close()
print('-------------')

# 외부 파일의 내용을 읽어들이기(반환하기)

# readline() 함수는 파일 첫번째 줄을 읽어들인다.
f = open('/Users/JKim/Desktop/source/g.txt','r')
read = f.readline()
print('g.txt-1st:',read) # g.txt-1st: Number is 1.
f.close()
print('--------------')

# 만약 전체 열(줄)을 다 읽어들이려면 WHILE 문을 써서 -
f = open('/Users/JKim/Desktop/source/g.txt','r')
while True:
    read = f.readline()
    if not read: break # if not = False
    print('WHILE :', read)
# WHILE :  Number is 1.
# WHILE :  Number is 2.
# WHILE :  Number is 3.
f.close()
print('---------------')

# read() 함수는 파일의 내용 전체를 문자열로 읽어들인다.
f = open('/Users/JKim/Desktop/source/g.txt','r')
all = f.read()
print(all)
f.close()
# Number is 1.
# Number is 2.
# Number is 3.
print('---------------')

# readlines() 함수는 각각의 줄을 요소로 하는 '리스트 ['한줄','두줄','세줄']형태'로 반환한다.
f = open('/Users/JKim/Desktop/source/g.txt','r')
lines = f.readlines()
print(lines) # ['Number is 1. \n', 'Number is 2. \n', 'Number is 3. \n'] 리스트로 출력됨.
f.close()

# 파일에 내용 추가하기 'a', w로 열면 기존 파일 내용 모두 없어져버림.
f = open('/Users/JKim/Desktop/source/new.txt','a')
f.write(' PYTHON') # What do I write something in here? 바로 뒤에 PYTHON 추가되었다.
f.close()

f = open('/Users/JKim/Desktop/source/new.txt','a')
f.write('\n2nd Line')
# What do I write something in here? PYTHON
# 2nd Line이 아래 줄 추가됨.
f.close()

f = open('/Users/JKim/Desktop/source/g.txt','a')
for i in range(5,8):
    f.write('Number is %d. \n' %i)
#Number is 1.
#Number is 2.
#Number is 3.
#Number is 5.
#Number is 6.
#Number is 7.
f.close()

# WITH AS F:형 구문을 쓰면 close()를 매번 써줄 필요가 없다.
with open('/Users/JKim/Desktop/source/with.txt', 'w') as f:
    f.write('Life is Short, WITH AS를 쓰면 매번 클로즈 할 필요 없어도 클로즈 된다.')

