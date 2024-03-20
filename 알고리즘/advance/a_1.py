import sys
sys.stdin = open('./A형 암벽등반.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())  # 맵의 N 세로 길이, M 가로 길이
    board = [list(map(int, input().split())) for _ in range(N)]
    G = tuple()
    # 시작 지점
    S = (N-1, 0)
    # 도착 지점 찾기
    for i in range(N):
        for j in range(M):
            if board[i][j] == 3:
                G = (i, j)
                break
        if G:
            break
    min_lev = N-1-G[0] # 최대 높이 = 바닥 - 골의 높이

    visited = [[[] for _ in range(M)] for _ in range(N)]
    dirx = [(0, 1), (0, -1)]  # DFS 탐색 경로
    diry = [(1, 0), (-1, 0)]  # DFS 탐색 경로

    def dfs(cur_pos, lev):
        # 종료 조건
        global min_lev
        if cur_pos == G:
            min_lev = min(min_lev, lev)
            return
        # 가지치기
        if lev >= min_lev:
            return

        cy, cx = cur_pos
        # 델타 방향으로 탐색
        for d in dirx:
            ny, nx = cy+d[0], cx+d[1]
            if 0 <= nx < M and board[ny][nx] != 0 and lev not in visited[ny][nx]:  # 모든 경로가 아니라 다른 레벨일 때만 탐색
                visited[ny][nx].append(lev)
                dfs((ny, nx), lev)

        for d in diry:
            # 수직 방향을로 가장 가까이 있는 발 디딜 수 있는 곳
            i = 1
            while i < N:
                ny, nx = cy+d[0]*i, cx+d[1]
                if 0 <= ny <N and board[ny][nx] != 0:
                    break
                i += 1
            next_lev = max(i, lev)  # 현재 탐색할 경로의 level
            if 0 <= ny < N and board[ny][nx] != 0 and lev not in visited[ny][nx]:
                visited[ny][nx].append(next_lev)
                dfs((ny, nx), next_lev)
    dfs(S,0)
    print(f'#{tc}', min_lev)



