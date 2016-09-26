#config=utf-8

print('')
scores = []
names = []
highscore = 0

fileopen = open('results.txt')
for line in fileopen:
    (name, score) = line.split() # split 내장함수는 왼쪽에 (,,, 여기서 콤마는 공백단위) 오른쪽에 .split()
    scores.append(float(score)) # append Method는 변수를 넣어라
    names.append(name)
scores.sort() # sort method는 낮은 것으로부터 높은 순으로 정렬, 거꾸로 정렬하는 것은 reverse(), 어차피 배열을 다루는 메소드니까 () 안에 float (score)를 넣을 필요가 없음
scores.reverse()
names.sort()
names.reverse()

print('The 1st score is :', names[0], scores[0])
print('The 2nd score is :', names[1], scores[1])
print('The 3rd score is :', names[2], scores[2])

fileopen.close()
