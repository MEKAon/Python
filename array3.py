a = int(input())
b = int(input())
c = int(input())

d = a*b*c

e = str(d)

#.count(숫자) = 리스트 (숫자)의 갯수를 구해줌
for x in range(0,10):
    print(e.count(str(x)))