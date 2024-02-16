# %%
# 최단 거리 탐색

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    Q = []
    start = tuple()
    
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)  # 시작점 찾기
                break
        if start :
            break
                
    dis_map = [[1e9] * N for _ in range(N)]    # 미로의 각 좌표마다 최소 이동 거리 저장
    dis_map[start[0]][start[1]] = 0           # 시작 좌표의 거리를 0으로 초기화
    result = 0

    Q.append(start)
    while Q:
        cur = Q.pop(0)

        for d in dirs:
            ni, nj = cur[0] + d[0], cur[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                if (arr[ni][nj] == 0 or arr[ni][nj] == 3) and visited[ni][nj] == 0:
                    Q.append((ni, nj))
                    visited[ni][nj] = visited[cur[0]][cur[1]] + 1
            if arr[cur[0]][cur[1]] == 3:
                result = visited[cur[0]][cur[1]] - 2    # 출발 위치와 도착 위치의 깊이를 빼 줌
                Q = []                                  # 탐색 성공 시 큐를 비움으로써 탐색을 종료
                break
                
    print(f'#{tc} {result}')