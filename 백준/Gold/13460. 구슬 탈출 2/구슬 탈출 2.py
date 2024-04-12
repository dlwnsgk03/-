from collections import deque

x_dir = [-1, 0, 1, 0]
y_dir = [0, 1, 0, -1]

def solution(N, M, graph):
    path = deque()
    path_score = {}
    

    def get_pos(c):
        for i in range(N):
            for j in range(M):
                if graph[i][j] == c:
                    return (i,j)
    
    red_pos = get_pos('R')
    blue_pos = get_pos('B')

    graph[red_pos[0]][red_pos[1]] = '.'
    graph[blue_pos[0]][blue_pos[1]] = '.'

    path.append(red_pos + blue_pos)
    path_score[red_pos + blue_pos] = 0

    red_first = False
    while path:
        curr_red_x, curr_red_y, curr_blue_x, curr_blue_y = path.popleft()

        for i in range(4):
            if x_dir[i] == -1:
                if curr_red_x < curr_blue_x:
                    red_first = True
            elif x_dir[i] == 1:
                if curr_red_x > curr_blue_x:
                    red_first = True
            elif y_dir[i] == -1:
                if curr_red_y < curr_blue_y:
                    red_first = True
            elif y_dir[i] == 1:
                if curr_red_y > curr_blue_y:
                    red_first = True

            next_red_x = curr_red_x + x_dir[i]
            next_red_y = curr_red_y + y_dir[i]
            next_blue_x = curr_blue_x + x_dir[i]
            next_blue_y = curr_blue_y + y_dir[i]

            if red_first:

                while graph[next_red_x][next_red_y] == '.':
                    next_red_x += x_dir[i]; next_red_y += y_dir[i]
                if graph[next_red_x][next_red_y] == '#':
                    graph[next_red_x - x_dir[i]][next_red_y - y_dir[i]] = 'R'

                while graph[next_blue_x][next_blue_y] == '.':
                    next_blue_x += x_dir[i]; next_blue_y += y_dir[i]

                graph[next_red_x - x_dir[i]][next_red_y - y_dir[i]] = '.'

            else:

                while graph[next_blue_x][next_blue_y] == '.':
                    next_blue_x += x_dir[i]; next_blue_y += y_dir[i]
                if graph[next_blue_x][next_blue_y] == '#':
                    graph[next_blue_x - x_dir[i]][next_blue_y - y_dir[i]] = 'B'
                
                while graph[next_red_x][next_red_y] == '.':
                    next_red_x += x_dir[i]; next_red_y += y_dir[i]

                graph[next_blue_x - x_dir[i]][next_blue_y - y_dir[i]] = '.'

            
            red_first = False

            if graph[next_blue_x][next_blue_y] == 'O':
                continue
            elif graph[next_red_x][next_red_y] == 'O':
                if path_score[(curr_red_x,curr_red_y, curr_blue_x, curr_blue_y)] + 1 < 11:
                    return path_score[(curr_red_x,curr_red_y, curr_blue_x, curr_blue_y)] + 1
            elif (next_red_x - x_dir[i], next_red_y - y_dir[i], next_blue_x - x_dir[i], next_blue_y - y_dir[i]) not in path_score:
                path_score[(next_red_x - x_dir[i], next_red_y - y_dir[i], next_blue_x - x_dir[i], next_blue_y - y_dir[i])] = path_score[(curr_red_x,curr_red_y, curr_blue_x, curr_blue_y)] + 1
                path.append((next_red_x - x_dir[i], next_red_y - y_dir[i], next_blue_x - x_dir[i], next_blue_y - y_dir[i]))

    return -1


N, M = map(int, input().split())

graph = [False for x in range(N)]
for i in range(N):
    x = list(input())
    graph[i] = x

print(solution(N,M,graph))