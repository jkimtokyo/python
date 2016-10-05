a = {'a':[1,2,3], 'b':[4,5,6]}

del a['b'] # delete a key, then del value also.
a['c'] = [7,8,9] # add a key - value pair
print(a['a']) # what values of 'a' ?

print(a.keys()) # key는 딕셔너리의 서브 펑션(함수)으로 에이의 키 값들을 반환한다.
print(a.values()) # key returns also values of a

for k in (a.keys()): # it used for in FOR, while....iteration syntax.
    print(k)
for v in (a.values()):
    print(v)

g = list(a.keys()) # 키 객체를 리스트로 반환, dict은 순서와 상관이 없다 반면 리스트와 튜플은 순서적이다.
print(g)

i = a.items() # 키 밸류 쌍을 얻기 위해선 아이템즈 펑션
print(i)
# 키로 밸류값 얻기 get
c = a.get('c')
print(c)

print(('name' in a)) # in 사용하여 키가 해당 딕에 있나 없나 조사. True or False 알기위해 그 자체를 프린트 해 버리면 출력창에 트루 펄스로 출력된다
print(('c' in a))

