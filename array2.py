#필요한 변수 만들기
max_num = 0
num = 0

for x in range(9):
    a = int(input())
    
    if a > max_num:
        max_num = a
        num = x+1

print('%d\n%d'%(max_num,num))