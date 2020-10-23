import sys

T = int(input())
for i in range(T):
    #sys.stdin.readline().split() = input().split()
    #속도 >
    a ,b = map(int, sys.stdin.readline().split())
    print(a+b)
