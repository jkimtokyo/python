# 집합 자료형이란, set로 만드는데 숫자형 리스트는 set([1,2,3])형태,문자형은 set('') 구문으로 생성한다. 집합 자료형이 유용할 때는 교집합 합집합 차집합을 구할 때다.
# 집합자료형은 중복을 허용하지 않고 순서가 없다.

s = set('hello') # 문자형이라서 []가 없다
print(s) # {'e', 'l', 'o', 'h'} > 중복 L 은 하나만 남았고 순서는 없다.

a = set([1,1,2,3,4,5,6])
b = set([4,4,5,6,7,8,9])

# 1.교집합 & , a.intersection(b)
print(a&b) # a & b 로 바로 교집합 구할 수 있다. 출력값은 {4, 5, 6}
print(a.intersection(b)) # same result

# 2.합집합 | '쉬프트 누른 상태에서 \ 키' 또는 a.union(b)
print(a|b) # {1, 2, 3, 4, 5, 6, 7, 8, 9}
print(a.union(b))

# 3.차집합 - 마이너스 또는 difference
print(a-b)
print(a.difference(b)) # {1, 2, 3}
print(b-a)
print(b.difference(a)) # {8, 9, 7}

# 집합자료형 함수들
# 값 1개를 추가하기 .add()
a = set([1,2,3])
a.add(4)
print(a) # 맨 뒤쪽에 4가 추가되어 {1, 2, 3, 4}

# 값 여러개를 추가하기 .update([])
a = set([1,2,3])
a.update([4,5])
print(a) # {1, 2, 3, 4, 5}

# 특정 값 삭제하기 remove()
b = set([1,2,3])
b.remove(2)
print(b) # {1, 3}
