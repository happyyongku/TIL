############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len, sum 함수를 사용하지 않습니다.
def average_cost(cost_list): 
    sum = 0
    for i in range(length(cost_list)):
        cost = cost_list[i]  # 리스트의 i 번째 요소를 cost로 지정
        sum += cost            # sum 에 cost를 더하고 다시 sum에 할당
    avg = sum/length(cost_list)  # for문을 끝낸 sum의 결과를 리스트의 길이로 나누기
    return avg
        

def length(iterable):
    cnt = 0
    for _ in iterable:  # 순회할 때마다 카운트를 1씩 올리고 카운트를 반환
        cnt += 1
    return cnt

# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(average_cost([25, 40, 50, 55]))  # 42.5
print(average_cost([60, 70, 90, 80, 100, 35])) # 72.5
#####################################################
