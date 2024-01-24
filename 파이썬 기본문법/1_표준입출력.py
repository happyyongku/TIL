#%%
# 표준 출력 print()

num = 20
name = '홍길동'
print('내 소개 :',name, ',',num)

#여러 줄을 동시에 입력

text = '''
Life is too short
You need python
'''

print(text)
# %%
# 문자열에 변수를 넣는 3가지 방법
# 1) % - 포맷팅
text = 'My name is %s, My age is %d' % ('홍길동', 30)
print(text)

text = 'My name is %s, My age is %d' % (name, num)
print(text)

# %s = 문자열, %d = 정수형
# %%
# 2) {} - 포맷팅

text = 'My name is {}, My age is {}' .format ('홍길동', 30)
print(text)

text = 'My name is {}, My age is {}' .format (name, num)
print(text)

#%%
# 3) f - 포맷팅 : python 3.6버전부터 지원
text = f'My name is {"홍길동"}, My age is {30}' 
print(text)

text = f'My name is {name}, My age is {num}' 
print(text)

# {}안에 표현식 <함수, 연산자, 변수 등의 처리결과>를 넣을 수 있음
text = f'My name is {name+"님"}, My age is {num+5}' 
print(text)

# %%
# 자릿수 및 정렬

text = 'My name is %20s, My age is %4d' % ('홍길동', 30)
print(text)

text = 'My name is %-20s, My age is %5.1f' % (name, 31.4321)
print(text)

# %s = 문자열, %d = 정수형
# 2) {} - 포맷팅
# > : 오른쪽 정렬, < : 왼쪽 정렬, ^ : 가운데 정렬
text = 'My name is {:>20}, My age is {:<20}' .format ('홍길동', 30)
print(text)

text = 'My name is {:^10}, My age is {:^10}' .format (name, num)
print(text)

floatnum = 31.4585

text = 'My name is {:^10}, My age is {:^10.1f}' .format (name, num)
print(text)

# 3) f - 포맷팅 : python 3.6버전부터 지원
text = f'My name is {"홍길동":>20}, My age is {30:<20}' 
print(text)

text = f'My name is {name:->20}, My age is {num:a^20}' 
print(text)

# {}안에 표현식 <함수, 연산자, 변수 등의 처리결과>를 넣을 수 있음
text = f'My name is {name+"님"}, My age is {num+5}' 
print(text)
# %%
# print() 끝문자 변경
print('사과')
print('포도')

#자동 개행을 없애고 싶을 때
print('사과', end=' ')
print('포도')

# %%
# 문자열 덧셈과 곱셈
# 문자열 덧셈
str1 = '사과'
str2 = '포도'
str3 = str1 + ' ' + str2
print(str3)

#문자열 곱셈
print(str1*3)
# %%
# 표준 입력
inStr = input() #키보드로부터 입력받아 문자열로 반환
print('문자열을 입력하세요 >', end='')# %%
print(inStr)

# %%
inStr = input('문자열을 입력하세요 >')
print(inStr)
# %%
numStr = input('정수를 입력하세요 :')
print(int(numStr) + 4)

# %%
mStr = float(input('정수를 입력하세요 :'))
print(mStr + 4)
# %%

# Quiz
# 섭씨 온도를 입력받아서 화씨 온도로 변환하는 프로그램 작성
# 화씨 온도 = 섭씨온도 * 1.8 + 32
# 화씨 온도를 출력할 때 소수점 둘째자리까지만 표시

celsius = float(input())
fahrenheit = celsius * 1.8 + 32
print(f'{fahrenheit:.2f}')