# 사용자 입력을 받기
# 사용자가 입력한 값을 변수에 대입하고 싶을 때 INPUT, input은 입력되는 모든 자료형을 문자열로 취급해서 받아들인다.
a = input('input something : ')
print(a)
# if user input number 3 숫자형을 입력해도 -
print(type(a)) # <class 'str'> 모든 자료형을 문자열로 취급해서 받아들인다.

# 프린트출력 알아보기
# ""만 써도 + 붙인것과 결과와 같다.
a = 'I''am''Jkim'
print(a)
b = 'I'+'am'+'Jkim'
print(b) # both a and b are same result IamJkim
# 문자열 띄어쓰기 하려면 , 구분하면 된다.
print('I','am','kim') # I am kim
