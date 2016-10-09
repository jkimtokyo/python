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

print('----------')

data = '101, john, USA, 8.32, fish, 21'
grut = {}
(grut['id'],grut['name'],grut['country'],grut['score'],grut['board'],grut['age']) = data.split(',') # split은 아무 것도 () 안에 넣지 않을 경우 빈칸을 기준으로 한다. 대신 , ; 둘 다 써봐도 문제 없이 작동된다
# key value dict 만들기 먼저 그릇 = {} 빈 그릇 만들고 a[key] = value 조합임 그런데 여기선 키가 문자열이기 때문에 '' 따옴표로.... 그리고 밸류를 스플릿 해서 하나씩 넣어야 하므로 data.split()
print(grut)
print('Country is :',grut['country'])

print('---------')

def finder_function(find_id):
    file_read = open('surfing_data.csv')
    for each_line in file_read:
        grut = {}
        (grut['id'],grut['name'],grut['country'],grut['score'],grut['type'],grut['age']) = each_line.split(';')
    if find_id == int(grut['id']):
        return(grut) # 그릇의 아이디 나이 등의 키가 아닌 1줄을 통째로 리턴한다

input_from = int(input('Type ID Here:'))
surfer = finder_function(input_from)
if surfer: # 그냥 이렇게 써도 트루 퍼스 구문이 된다...
    print(surfer['id'],surfer['name'],surfer['country'],surfer['score'],surfer['type'],surfer['age'])