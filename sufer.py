# config=utf-8

high_score = 0
openfile = open('results.txt')
for read in openfile:
    (a,b) = read.split()
    if float(b) > high_score:
        high_score = float(b)
print(high_score)

