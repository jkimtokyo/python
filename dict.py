# 이 책에서는 dict를 해쉬로 표현함 key - value list
#config = utf-8
scores = {} # 빈 해쉬 딕을 선언
result = open('results.txt') # 오픈 펑션은 파일 펑션의 하부 펑션으로 파일 열기
for x in result: # x is variable, 인 뒤에 대상,
    (name, score) = x.split() # 공백기준()으로 하나는 네임으로 하나는 스코어로 넣어라
    scores[score] = name
result.close()
print('Top score point')
for each_score in sorted(scores.keys(), reverse = True):
        print(scores[each_score] + ' : ' + each_score)

print('------------------')

def finddetails(idfind):
    sufer = open('surfing_data.csv')
    for each_line in sufer:
        s = {}
        (s['id'],s['name'],s['country'],s['average'],s['board'],s['age']) = each_line.split(';')
        if idfind == int(s['age']):
            #sufer.close()
            return (s)
    #sufer.close()
    return({})

lookup = int(input('Enter the age: '))
suferid = finddetails(lookup)
print(suferid)
#if suferid:
#    print('id:'+suferid['id'],', name:'+suferid['name'],', country:'+suferid['country'],', average:'+suferid['average'],', board:'+suferid['board'],', age:'+suferid['age'])

print('------------------')
def prediction(finding):
    file = open('predict.csv')
    for each_line in file:
        sp = {}
        (sp['num'],sp['month'],sp['4%'],sp['5%'],sp['6%'],sp['7%'],sp['8%'],sp['9%'],sp['10%']) = each_line.split(';')
        if finding == sp['month']:
            file.close()
            return (sp)
    file.close()
    return({})

lookup = int(input('Enter the Month: '))
value = prediction(finding)
if question:
    print('num'+value['num'],'Month:'+value['month'],'4:'+value['4%'],'5:'+value['5%'],'6:'+value['6%'],'7:'+value['7%'],'8:'+value['8%'],'9:'+value['9%'],'10:'+value['10%'])
