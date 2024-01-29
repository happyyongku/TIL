############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 리스트 메서드 .count()를 사용하지 않습니다.
def get_count(iterable,value): 
    cnt = 0  # 초기 카운트 0
    for char in iterable:  # 순회가능한 요소를 순회하며
        if char == value:   # 요소가 찾으려는 value와 같으면
            cnt += 1       # 카운트에 1 더하기
    return cnt    # 카운트 반환

def tidy_up_company(email_list):
    new_dict = {}   # 새 딕셔너리 생성
    for email in email_list: # email_list를 순회하며 찾을 email을 설정
        count = get_count(email_list,email)  # email_list내에 email이 얼마나 있는지 카운트
        new_dict[email] = count  # 새 딕셔너리에  email을 키로, count를 값으로 가지는 딕셔너리 생성
    return new_dict  # 딕셔너리 반환



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
email_list1 = ['Koogle', 'Koogle', 'Maver']
print(tidy_up_company(email_list1))   # {'Koogle': 2, 'Maver': 1}

email_list2 = [
    'Koogle', 'Koogle', 'JCloud', 'Koogle', 'GaKao', 
    'School', 'Koogle', 'Maver', 'GaKao', 'Maver', 
    'Koogle', 'GaKao', 'School', 'GaKao', 'JCloud', 
    'School', 'GaKao', 'GaKao', 'Maver', 'Koogle'
]
print(tidy_up_company(email_list2))
# {'Koogle': 6, 'JCloud': 2, 'GaKao': 6, 'School': 3, 'Maver': 3}
#####################################################
