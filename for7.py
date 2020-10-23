a = int(input())

for x in range(a):
    b,c = map(int,input().split())
    d = b+c
    print('Case #%s: %s' %(x+1,d))