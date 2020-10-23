a, b = map(int,input().split())

#리스트를 쓰기위해서 list()를 사용
c = list(map(int,input().split()))

for x in range(a):
    if c[x] < b:
        print(c[x], end=' ')