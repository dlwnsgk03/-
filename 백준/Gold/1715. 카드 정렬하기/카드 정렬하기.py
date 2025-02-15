from sys import stdin
import heapq

N = int(input())
num_list = []

for _ in range(N):
    heapq.heappush(num_list, int(stdin.readline()))

# print(num_list)
total = 0
length = len(num_list)
while length > 1:
    num1 = heapq.heappop(num_list)
    num2 = heapq.heappop(num_list)
    new_num = num1+num2
    total += new_num
    heapq.heappush(num_list, new_num)
    length -= 1
# if length == 1:
#     total += heapq.heappop(num_list)

print(total)