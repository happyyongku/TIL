# %%
# 최단 거리 탐색

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    Q = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)  # 시작점 찾기
                break
                
    visited = [[0] * N for _ in range(N)]       # 탐색 깊이 저장 용도로 사용
    result = 0

    visited[start[0]][start[1]] = 1             # 탐색 깊이 저장
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