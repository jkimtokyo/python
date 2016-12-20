# 딕셔너리 자료형에서 딕셔너리는 '사전' 의미로 {키:밸류} 형태의 1:1 묶음이다. 해쉬 라고 부른다 다른 언어들에선-
# 앞 키에는 변하지 않는 값을 사용하고 뒤 밸류에는 변수, 그래서 앞 키 부분에 리스트는 사용불가지만 튜플은 사용 가능하다. 밸류부분은 상관 없음.

dic = {1:'a','second':'b',3:'c',4:'d'} # 키는 고유라서 중복되어 사용하면 안된다.
print(dic[1]) # a
print(dic['second']) # b

# 딕셔너리의 밸류 부분에 리스트도 넣을 수 있다.
dic = {1:[1,2,3]}
print(dic[1]) # [1,2,3]

# 딕셔너리 키:밸류 쌍 추가하기
jk = {'year':'1970'}
jk['month'] = '01' # 딕[키] = 밸류
jk['day'] = '18'
print(jk) # {'day': '18', 'year': '1970', 'month': '01'} 쌍의 순서는 출력 때마다 그때 그때 달라요.

# 이번엔 삭제 del dic[key]
#del jk['day','month'] # 이렇게 복수개 콤마로 하면 에러난다.
del jk['month']
print(jk) # {'day': '18', 'year': '1970'}

# 함수 중에서 키 들만 모아서 리스트로 만들어 주는 list(dic.keys())
print(list(jk.keys())) # 괄호가 많아 지저분하지만 어쨌거나 ['day', 'year'] 리스트로 키들을 출력한다.
# 한편 리스트까지 만들어 출력하진 않지만 dic.keys() 구문은 반복문에 바로 사용할 수 있다.
for i in jk.keys():
    print(i,'',end='') # year day 출력됨

# 이번에는 밸류들을 리스트로 만들어 주는 dic.values()
v = jk.values()
print(v) # ['1970', '18'] 출력됨
for i in jk.values():
    print(i,'',end='') # 1970 18

# 이번에는 키밸류를 쌍으로 묶어서 튜플로 만들어 주는 .items()
print(jk.items()) # ([('year', '1970'), ('day', '18')])

# 키 밸류 전부 삭제하기 .clear()
jk.clear()
print(jk) # {} 지워졌음

# 키를 참조해서 밸류를 가져오기 .get(), 이것은 dic[]과 동일하게 기능하지만 키 값이 없을 경우 에러가 아니라 None을 출력하는 점이 틀리다.
kim = {'first':'J','last':'Kim','phone':'09084648502'}
print(kim.get('a'))  # None 출력한다.

# 키가 딕셔너리 안에 있는지 없는지를 조사한다 in 트루 펄스로 값 출력되는 형태다.
print('age' in kim) # False
print('phone' in kim) # True
