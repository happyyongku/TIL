import sys
sys.stdin = open('./A형 전기충전소.txt')

#
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    homes = [list(map(int, input().split())) for _ in range(N)]  # [x, y, 거리]
    board = {(i, j): [set(), [0]*N] for i in range(-15, 16) for j in range(-15, 16)}
    #        key : 좌표, value : [set(가능한 집 인덱스), list(각 집마다의 거리)]
    # board = {}
    # for i in range(-15, 16):
    #     for j in range(-15, 16):
    #         board[(i, j)] = [set(), [0]*N]

    home_poses = [(h[0], h[1]) for h in homes]
    max_dis = 60*N
    min_all_cross = max_dis
    search_poses = []
    for i, (x,y,dis) in enumerate(homes):
        for ky in range(-dis, dis+1):
            for kx in range(-dis+abs(ky), dis+1-abs(ky)):
                nx, ny = x + kx, y + ky
                if -15 <= nx <= 15 and -15 <= ny <= 15 and (nx, ny) not in home_poses:
                    board[(nx, ny)][0].add(i)
                    board[(nx, ny)][1][i] = abs(kx) + abs(ky)
                    search_poses.append((nx, ny))

                    if len(board[(nx, ny)][0]) == N:
                        # 최소 거리 저장
                        min_all_cross = min(min_all_cross, sum(board[(nx, ny)][1]))

    result = max_dis # 최종 결과값 저장 변수
    if min_all_cross != max_dis :
        result = min_all_cross
    else:
        # 충전소 2개로 최소 거리 판단
        while search_poses :
            cx, cy = search_poses.pop()  # 충전소 위치 1 (기준)
            c_home, c_dis = board[(cx, cy)]
            for nx, ny in search_poses :  # 나머지 충전소 위치
                n_home, n_dis = board[(nx, ny)]
                # 2개의 충전소ㅗ 모든 집 커버 가능할 때만 result 업데이트
                if len(c_home | n_home) == N :  # |는 합집합 기호
                    # 두 충전소 간의 최소 거리
                    inter_home = c_home & n_home
                    cur_dis = sum(c_dis) + sum(n_dis) - sum(max(c_dis[i], n_dis[i])for i in inter_home)
                    result = min(result, cur_dis)
        if result == max_dis: # 2개의 충전소로 커버 안되는 경우
            result = -1
    print(f'#{tc}', result)
