# %%
# 최단 거리 탐색

dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]
    Q = []
    # 가중치가 있는 그래프에서 최단 혹은 최소등 최적 값을 찾기위한 방법
    
    start = tuple()
    G = tuple()
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:
                start = (i, j)  # 시작점 찾기
            
            if arr[i][j] == 3:
                G = (i, j)
        
                
    dis_map = [[1e9] * N for _ in range(N)]    # 미로의 각 좌표마다 최소 이동 거리 저장
    dis_map[start[0]][start[1]] = 0           # 시작 좌표의 거리를 0으로 초기화
    result = 0

    Q.append(start)
    while Q:
        cur = Q.pop(0)
        # if arr[cur[0]][cur[1]] == 3:    # 갈 수 있는 경로가 하나일 때
        #     result = dis_map[ni][nj]
        #     break
        
        for d in dirs:
            ni, nj = cur[0] + d[0], cur[1] + d[1]
            if 0 <= ni < N and 0 <= nj < N:
                dis_map[ni][nj] = min(dis_map[ni][nj], dis_map[cur[0]][cur[1]] + 1)
                if arr[ni][nj] in [0, 3]:
                    arr[ni][nj] = 1  # 통로
                    Q.append((ni, nj))
                    
                    
                
    print(f'#{tc} {result}')
    print(f'#{tc} {dis_map[G[0]][G[1]]}')