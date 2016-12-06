# 리스트 자료형이란 집합이다
list = [1,2,3,4,'a','b','c']
list2 = [1,2,[3,4,5],'a','b'] # 집합 안에 또 집합

# 인덱싱 - 순서 알아내기
i = list[0] + list2[0]
print(i) # 2

# [-1]은 리스트의 마지막 요소
print(list[-1]) # c
print(list2[-1]) # b 만약 부분집합에서 하나를 꺼내려면 순서대로 [][] (콤마 없음)
print(list2[-3][-1]) # 5, 부분 집합이 몇개라도 상관 없이 [][]
print('')

# 슬라이싱 : 슬라이싱이란 ~부터 ~까지 [n:n]
print(list[1:2]) # 1번째부터 2번째까지, 이 때 마지막 수(2번째)는 포함되지 않는다. [2]
print(list2[2][0:2]) # [3, 4]
print(list[5:]) # '5번째 요소'부터 뒤의 요소 전부란 구문임 ['b', 'c']
print(list[:2]) # 앞에서부터 '2번째 요소'까지 그래서 여기선 [1,2]
print(list2[2][1:]) # [4, 5]
print('')

# 리스트연산자 : 집합 즉 리스트도 연산이 된다.
a = [1,2]
b = [3,4]
print(a+b) # [1,2,3,4]
#print(a*b) # TypeError: can't multiply 에러. 리스트끼리 곱하기 안된다. 반복만 된다. 그리고 숫자와 문자도 연산 안된다.
print(b*2) # [3, 4, 3, 4] 2회 반복
a = ['a','b']
print(a*2) # ['a', 'b', 'a', 'b'] 2회 반복

# 리스트의 변경: 리스트에서 하나의 요소를 변경하기
a = [1,2,3,4]
a[1] = ['z','x']
a[3] = 8
print(a) # [1, ['z', 'x'], 3, 8]

# 리스트에서 연속되는 복수의 요소를 한꺼번에 변경하기
a[1:3] = ['a','b','c'] # 1번째인 ['z', 'x'] 부터 2번째인[3], 마지막 3번째는 포함 안되니까
print(a) # [1, 'a', 'b', 'c', 8]

# 리스트에서 요소 삭제하기 del
a = [1,2,3,4,5]
del a[0] # [2, 3, 4, 5]
del a[0:3] # 0번째부터 3번째 마지막 3번째는 포함 안되니까
print(a) # [5]만 남았다.

# 리스트에서 요소 삭제하기 []
a = [1,2,3,4,5]
a[0:4] = []
print(a) # [5]만 남았다.

# 리스트 맨 뒤로 요소 추가하기 .append(요소)
a = [1,2,3]
a.append(4)
print(a) # [1,2,3,4]
a.append([5,6])
print(a) # [1, 2, 3, 4, [5, 6]]

# 리스트 안 요소들을 정렬하는 .sort() : 숫자 혹은 알파벳 순서
a = [1,5,2,8]
a.sort() # [1, 2, 5, 8]
print(a)
# 만약 [1,5,2,8,3,'a','z','g'] 이렇게 혼용되어 있으면 TypeError: unorderable types: str() < int()

# 리스트를 역순으로 뒤집기 .reverse() : 순서를 정렬한 후 뒤집는 게 아니다.
a = [1,3,2,'z','g']
a.reverse()
print(a) # ['g', 'z', 2, 3, 1]

# 위치값 출력(반환) 인덱스라고도 함. .index(요소)
a = [0,1,'a',3,4,5]
#print(a.index(2)) # ValueError: 2 is not in list : 이건 리스트의 0,1,2번째 요소인 a를 가져오는 것이 아니다. 리스트 안에 있는 요소가 몇 번째인지를 가져오는 것이다
print(a.index('a')) # 출력값은 2(번째)

# 리스트에 요소를 삽입하기 .insert(번째,요소)
a = [0,1,2,3]
a.insert(4,4) # 앞 숫자가 번째, 뒤가 삽입할 요소 [0, 1, 2, 3, 4]
print(a)
# a.insert(0:1,1) # 이렇게 범위 안에 삽입은 불가함 invalid syntax

# 리스트에서 요소를 삭제하기 .remove(요소)
a = [1,2,3,4]
a.remove(2)
print(a) # [1, 3, 4]
a = [1,2,3,4,1,2,3,4] # 만약 똑같은 요소가 중복되어 들어있을 경우 맨 앞의 것만 리무브.
a.remove(2) # [1, 3, 4, 1, 2, 3, 4]

# 리스트에서 n번째 요소를 삭제하기 .pop(번째)
a = [1,2,3]
a.pop(0)
print(a) #[2, 3]
a.pop()
print(a) # 만약 .pop() 공란으로 쓰면 맨 뒷 요소를 삭제한다. [2]

# 리스트 내에 그 요소가 몇 개인지 세어보기 .count(요소)
a = [1,2,3,4,1,2,3,4,2]
print(a.count(2)) # 3
