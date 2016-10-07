# config=utf-8
# list and sort
score = []
name = []
file = open('results.txt')
for read in file:
    (a,b) = read.split()
    name.append(a)
    name.sort() # 숫자가 아닌 문자는 a,b,c,d 순으로 소트가 된다..
    score.append(b)
    score.sort(reverse = True)
   #print(name, score)
print('-----------')

# dictionary
grut = {} # 먼저 빈 딕을 만들어둔다. 리스트 만들 때도 마찬가지로 빈 리스트 그릇 만들어둔다
file = open('results.txt')
for read in file:
    (name,score) = read.split() #파일 안에 공백을 갈라서 앞의 것을 네임으로 뒷 것을 스코어 변수에 할당
    grut[score] = name # dict 괄호 안의 것이 키고 = 뒤의 것이 밸류다. 그런데 복수의 키가 같은 값을 가지면 아래에서 넣은 값이 출력된다. score 순으로 정렬을 해줘야 하기 때문에 키 값으로 점수를 넣는다....
    #print(pair) # pair를 그대로 출력해보자' 포를 썼으니까 하나씩 하나씩 추가되어 나온다;
print('')
for key in grut.keys(): # 키 함수는 딕에서 쓸 수 있는데 키들을 배열로 만든다
    print(grut[key] + ' : ' + key)