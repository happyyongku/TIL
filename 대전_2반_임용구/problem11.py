############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def length(iterable):   # 순회할 때마다 카운트를 1씩 올리고 카운트를 반환
    cnt = 0
    for _ in iterable:
        cnt += 1
    return cnt

def get_final_position(N, matrix, move_list):
    loc = [] # 초기 위치를 저장할 리스트
    for i in range(length(matrix)):
        for j in range(length(matrix[i])):  # matrix를 순회하며 1울 찾고 그 1의 인덱스 값을 저장
            if matrix[i][j] == 1:
                loc.append(i)
                loc.append(j)
                           
    for move in move_list:  # move_list를 순회하며 move에 맞게 loc의 값을 변경
        if move == 0:
            loc[0] -= 1
        elif move == 1:
            loc[0] += 1
        elif move == 2:
            loc[1] -= 1
        elif move == 3:
            loc[1] += 1
        if loc[0] < 0 or loc[1] < 0 or loc[0] >= N or loc[1] >= N: # 만약 움직였을 때 loc의 두 값 중 어느 하나라도 0 미만이면 None을 반환
            return None
    return loc   # 전부 움직였을 때의 위치를 반환
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
N = 3
matrix = [
    [1, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
] 
moves1 = [1, 1, 3]
print(get_final_position(N, matrix, moves1)) # [2, 1]

moves2 = [1, 2, 3, 3]
print(get_final_position(N, matrix, moves2)) # None
#####################################################
