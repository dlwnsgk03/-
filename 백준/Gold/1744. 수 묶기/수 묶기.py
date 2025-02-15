from sys import stdin

N = int(stdin.readline())

neg_num = []
pos_num = []
total = 0

for i in range(N):
    num = int(stdin.readline())
    if num <= 0:
        neg_num.append(num) # 0이 neg에 들어가면 없애줄 수 있음
    elif num > 1:
        pos_num.append(num)
    else:
        total += 1 # 1은 더하는게 무조건 이득이라

neg_num.sort()
pos_num.sort(reverse = True)

neg_len = len(neg_num)
pos_len = len(pos_num)

for i in range(0, neg_len, 2):
    if i+1 >= neg_len:
        total += neg_num[i] # 마지막 수
    else:
        total += neg_num[i]*neg_num[i+1]

for i in range(0, pos_len, 2):
    if i+1 >= pos_len:
        total += pos_num[i]
    else:
        total += pos_num[i]*pos_num[i+1]

print(total)