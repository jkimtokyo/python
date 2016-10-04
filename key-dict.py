a = {'a':[1,2,3], 'b':[4,5,6]}

del a['b'] # delete a key, then del value also.
a['c'] = [7,8,9] # add a key - value pair

print(a['a']) # what is value of 'a' ?

print(a.keys()) # key는 딕셔너리의 서브 펑션(함수)으로 에이의 키 값들을 반환한다.
print(a.values()) # key returns also values of a

for k in (a.keys()): # it used for in FOR, while....iteration syntax.
    print(k)
for v in (a.values()):
    print(v)

