from sys import stdin
import heapq

N = int(stdin.readline())
arr = [[0]*2 for _ in range(N)]

for i in range(N):
    arr[i][0], arr[i][1] = map(int, stdin.readline().split())

arr.sort()
lines = arr[0]

total_length = 0

for i in range(1, N):
    if arr[i][0] <= lines[1] and arr[i][1] > lines[1]:
        lines[1] = arr[i][1]
    elif arr[i][0] > lines[1]:
        total_length += lines[1] - lines[0]
        lines[0] = arr[i][0]
        lines[1] = arr[i][1]

total_length += lines[1] - lines[0]
print(total_length)