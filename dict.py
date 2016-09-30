# 이 책에서는 dict를 해쉬로 표현함 key - value list
#config = utf-8

scores = {}

result = open('results.txt')
for line in result:
    (name, score) = line.split()
    scores[score] = name
result.close()

print('Top score is: ')

for each_score in scores.keys():
        print('Sufer' + scores[each_score] + 'scored' + each_score)
