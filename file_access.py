#config=utf-8

highscore = 0

fileopen = open('results.txt')
for line in fileopen:
    (name, score) = line.split()
    if float(score) > highscore:
        highscore = float(score)
    print(score)
fileopen.close()
print(score)