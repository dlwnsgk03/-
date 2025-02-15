from sys import stdin
import heapq

N = int(stdin.readline())

arr = [[0]*2 for i in range(N)]

for i in range(N):
    arr[i][0], arr[i][1] = map(int, stdin.readline().split())

arr.sort()

end_time = []
heapq.heappush(end_time, arr[0][1])

for i in range(1,N):
    if arr[i][0] >= end_time[0]:
        heapq.heapreplace(end_time, arr[i][1])
    else:
        heapq.heappush(end_time,arr[i][1])

print(len(end_time))