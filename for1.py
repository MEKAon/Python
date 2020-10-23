a = int(input())

if 0 < a < 10:
    for x in range(1, 10):
        print("%d * %d = %d" %(a,x,a*x))