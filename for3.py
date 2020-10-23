a = int(input())
i = 0
cnt = 0

for x in range(0,a):
    i = i+1
    cnt = cnt + i
    if i == a:
        print(cnt)

# 모범 답안
# a = int(input())
# sum = 0
# for i in range(a+1):
#     sum = sum + i
# print(sum)