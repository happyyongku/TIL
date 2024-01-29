############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def length(iterable):    # 순회할 때마다 카운트를 1씩 올리고 카운트를 반환
    cnt = 0
    for _ in iterable:
        cnt += 1
    return cnt

def get_count(iterable,value): 
    cnt = 0  # 초기 카운트 0
    for char in iterable:  # 순회가능한 요소를 순회하며
        if char == value:   # 요소가 찾으려는 value와 같으면
            cnt += 1       # 카운트에 1 더하기
    return cnt    # 카운트 반환

def find_solo(number_list):
    error = None  # 초기 에러는 None
    for num in number_list:  # 주어진 리스트를 순회하며
        count = get_count(number_list,num)  # 그 숫자의 수를 카운트
        if count % 2 != 0:   # 만약 그 숫자를 카운트한 수가 홀수라면
            error = num  # 에러를 그 숫자로 할당
    return error # 에러 반환
    
    



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
number_list1 = [64, 27, 71, 27, 64]
print(find_solo(number_list1))  # 71
number_list2 = [4, 14, 60, 14, 49, 49, 78, 60, 78]
print(find_solo(number_list2))  # 4
#####################################################