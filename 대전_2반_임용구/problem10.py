############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    loc = []
    for num in current:  # 튜플을 조작하기 위해 튜플의 요소를 순회하며 리스트에 삽입
        loc.append(num)
        
    if M == 0:
        loc[0] -= 1    # M의 값을 0,1,2,3 에 따라 좌표를 변경
    elif M == 1:
        loc[0] += 1
    elif M == 2:
        loc[1] -= 1
    elif M == 3:
        loc[1] += 1
    
    if loc[0] >= 0 and loc[1] >= 0 and loc[0] < N and loc[1] < N:  # 만약 loc의 1,2번째 요소가 0이상이면 True
        return True
    else:
        return False  # 아니라면 False
        
    
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
