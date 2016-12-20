# 반복문, 기본적 구문은 FOR 변수 in 리스트 (튜플 혹은 문자열):

list = ['one', 'two', 'three']
for i in list:
    print(i)  # 출력값은 one two three

list = [(1, 2), (3, 4)]
for (a, b) in list:
    print(a + b)  # 3 7 list의 요소값이 튜플이기 때문에 각각의 요소들이 자동으로 (a,b) 변수에 대입된다.

# FOR문의 응용
# 차례차례 참 거짓 판단
point = [90, 47, 62]
for i in point:
    if i >= 60:
        print('PASS')
    else:
        print('FAIL')  # PASS  FAIL  PASS

# FOR 그리고 continue, for 문장 내에서 '참일 때 continue'를 만나면 for 문의 처음으로 돌아가 다음 것으로. 무시하고 'NEXT'
point = [91, 23, 47, 51]
num = 0
for i in point:
    num = num + 1
    if i < 50: continue
    print('%d' % num, 'SUCCESS')  # 1 SUCCESS  4 SUCCESS

# FOR 그리고 range 함수, range 함수는 0부터 () 안의 숫자 미만까지를 객체로 만든다. range(2)라면 0,1 시작과 끝을 표기하려면 range(1,3) 이건 1,2
sum = 0
for i in range(10):
    sum = sum + i
print(sum)  # sum = 0+0=0,0+1=1,1+2=3,3+3=6,6+4=10,10+5=15,15+6=21,21+7=28,28+8=36,36+9=45

num = 0
for i in range(1, 5):  # 1 포함 4까지
    num = num + i
print(num)  # num = 0+1=1,1+2=3,3+3=6,6+4=10

# range와 len 함수 조합형 range(len()), len 함수는 리스트 요소의 갯수를 돌려주는 함수
list = [40, 50, 60]
print(len(list))  # 3

list = [91, 23, 47, 51]
num = 0
for i in range(len(list)):  # = range(4)
    num = num + 1
    if list[i] < 50: continue  # 이건... 리스트형을 좀 봐야겠군.
    print('%d' % num, 'SUCCESS')  # 1 SUCCESS  4 SUCCESS

# FOR, Range를 2개 반복해서 구구단 만들기
for x in range(1, 10):
    for y in range(2, 10):  # 들여쓰기 안하면 오류
# print(x*y) # 이렇게 들여쓰기 안하면 오류
        print(x * y)  # 이렇게 두번째 FOR 아래 들여쓰기 해야 됨

# range()에서 숫자들이 어떻게 대입되는가.. x가 1일 때 다음 y의 2,3,4...9까지를 반복 후 x 2가 또 다음 FOR
for x in range(2, 10):
    for y in range(1, 10):  # 들여쓰기 안하면 오류
        print(x * y, end='')  # end='' 이것을 삽입해 주면 한줄로 출력된다 246810121416183691215182124274812162024283236510152
        # print('') # '' 삽입해 주면 결과값이 한 줄씩 출력된다
    print('')  # 들여쓰기를 FOR에 맞춰주면 24681012141618 줄바꿈 369121518212427 형태

# 리스트 내포(LIST Comprehension) 문장
# 문법은 [식 for i in list]
a = [1,2]
b = [i for i in a] # 출력값은 [1,2] 이건 식이 없는...
a = [1, 2, 3]
b = [i+1 for i in a] # 1)for i in a 하나씩 가져와서 2)i+1 대입
print(b)
print('------------')

# 리스트 내포(LIST Comprehension) 문장에는 if 문도 들어갈 수 있다 [식 for i in list if 조건식]
a = [3,4,5,6,7]
b = [i for i in a if i%2 == 0] # list 하나씩 들고 와서 그것이 만약 짝수(2로 나눠 나머지가 0이라면(i%2==0)) i
print(b) # [4, 6]
c = [i*3 for i in a if i%2 == 1] # list 하나씩 들고 와서 그것이 홀수면 if i%2 == 1 i*3
print(c) # [9, 15, 21]
f = [i+1 for i in a if i==7] # 8, 왜 7이 아닌 8이 출력되는가??
# 구문해석의 순서: 1)for i in a : 리스트에 있는 i 들을 순서대로 가져온다. 2)if i==7 그 중 7과 같은... 3)i+1 계산.

# 리스트 내포 문장에서 복수의 FOR IF 사용할 수 있다
a = [1,2,3,4,5]
b = [4,5,6,7,8]
c = [i+j for i in a if i>1
         for j in b if i==j] # 들여쓰기 해야 함
# 1)for i in a a의 리스트들 > 2)1보다 큰 a 2,3,4
# 3)for j in b : 1보다 큰 a의 2,3,4를 아랫 줄 b의 4,5,6,7과 참조하여 -
# 4)i == j 조건은 4와 5가 해당
# 5)4+4, 5+5 출력값은 [8, 10]
print(c) # 8

a = [1,2,3,4,5]
b = [1,2,3,4,5]
c = [j+1 for i in a if i == 2
        for j in b if i == j]
# for i in a > if i == 2 > 그 아래 FOR 문 for j in b > i == j > j+1
print(c) # 3
