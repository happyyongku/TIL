# %%
t1 = (1,2,['사과','포도'])
print(t1)
print(t1[2][0])
print(t1[-1][0])

t1[2][0] = '귤'

print(t1)
# %%
d1 = {'사과':3,'포도':1}
print(d1)
del d1['사과'] # del은 딕셔너리의 값을 삭제
d1['사과쨈'] = 3
print(d1)
# %%
# --------
# 딕셔너리 순서 만들기
d1 = {'사과':3,'포도':1, '귤':5}

#순서 만들기
key_index = {0 :'귤', 1:'사과', 2:'포도'}

for i in range(3):
    print(d1[key_index[i]])
# %%

#논리 연산자
# and (&)
print(True and True) # True
print(True & True) # True
print(True and False) # False
print(True & False) # False
# &는 비트의 and연산으로도 사용
# 1011 & 0001 => 0001
print(0b1011 & 0b0001)  # 1


# or (|)
print(True or True) # True
print(True | True) # True
print(True or False) # True
print(True | False) # True
print(False | False) # False
# |는 비트의 and연산으로도 사용 
# 1011 | 0001 => 1011
print(bin(0b1011 | 0b0001)) # bin() 10진수 -> 2진수
# %%
# not 논리 반전
print(not True) # False
print(not False) # True

#xor : ^
# 다르면 참, 같으면 거짓
print(True ^ False) # True
print(True ^ True) # False
print(False ^ False) #False

# 비트 xor연산 가능
print(0b1011 ^ 0b0001)
print(bin(0b1011 ^ 0b0001)) # bin() 10진수 -> 2진수