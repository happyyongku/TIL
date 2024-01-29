############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 내장 함수 len 함수를 사용하지 않습니다.
def length(iterable):  # 순회할 때마다 카운트를 1씩 올리고 카운트를 반환
    cnt = 0
    for _ in iterable:
        cnt += 1
    return cnt

def compare_pw(user):
    if length(user['password']) >= 8 and length(user['password']) < 32:  # password를 키로 갖는 값의 길이가 8이상 32 미만인지 확인
        if user['password'] == user['password_confirm']:  # 그 값이 password_confirm 의 값과 같은지 확인
            return True  # 맞다면 True
        else:
            return False   # 다르다면 False
    else :
        return False
    


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
user_data1 = {
    'user_id': 'leessafy24',
    'password': 'q1w2e3r4',
    'password_confirm': 'q1w2e3r4',
    'email': 'goodjob24@mail.com',
}
print(compare_pw(user_data1))  # True

user_data2 = {
    'user_id': 'edu',
    'password': 'q1w2e3r4',
    'password_confirm': 'asdf123',
    'email': 'mail24.mail.com',
}
print(compare_pw(user_data2))  # False
#####################################################
