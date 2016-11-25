# 인수에 True False
def truefalse(a=True):
    if a:
        print('I am a Man')
    else:
        print('Women')
print(truefalse()) # 출력값은 I am a Man, 아무 값도 없을 때는 위에서 설정한 초기값을 따른다.
print(truefalse(False)) # 출력값은 우먼
print(truefalse('a')) # 출력값은 I am a Man
print(truefalse('b')) # 출력값은 I am a Man
# *True의 반대는 '그 밖에'가 아니라 False다.

# 함수 내부에서 만든 (할당한) 변수의 범위는 함수 안에서만 통용된다.

