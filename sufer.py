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
grut = {} # 먼저 빈 딕그릇을 만들어 둔다. 리스트 만들 때도 마찬가지로 빈 리스트그릇 만들어둔다
file = open('results.txt')
for file_read in file:
    (name,score) = file_read.split() #파일 안에 공백을 갈라서 앞의 것을 네임으로 뒷 것을 스코어 변수에 할당
    grut[score] = name
    # dict 괄호 안의 것이 키고 = 뒤의 것이 밸류다. 그런데 복수의 키가 같은 값을 가지면 아래에서 넣은 값이 출력된다. score 순으로 정렬을 해줘야 하기 때문에 키 값으로 점수를 넣는다....
    #print(pair) # pair를 그대로 출력해보자' 포를 썼으니까 하나씩 하나씩 추가되어 나온다;
print('')
for score_value in grut.keys(): # 키 함수는 딕에서 쓸 수 있는데 키들을 배열로 만든다 즉 키들을 스코어 밸류라는 변수에 넣어라..
    print(score_value, grut[score_value]) # 키에 해당되는 밸류값 가져 오는 것은 a[키] 하면 밸류를 소환한다.
print('----------')
# dic -> sorting
second_grut = {}
open_file = open('results.txt')
for vals in open_file:
    (a,b) = vals.split() # a에는 이름이 b에는 점수가
    second_grut[b] = a # b 점수를 키 값으로 하고 거기에 이름들을 할당 결국 b:a 구조 마들기
    #print(second_grut)
for list in sorted(second_grut.keys(), reverse = True): # for 문과 함께 sorted() 함수를 통해
    print(list, second_grut[list])
    open_file.close()

