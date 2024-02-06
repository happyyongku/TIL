
# 델타 문제
# 이차원 리스트에서 각 요소와 인접한 값들 간의 절댓값의 총 합을 얻어야 함
import sys
sys.stdin = open('./deta_in.txt')

dirs = [(1,0),(-1,0),(0,1),(0,-1)]  # (y방향, x방향)
# diry = [1,-1,0,0]
# dirx = [0,0,1,-1]

for tc in range(1,11) :
    n = int(input())
    board = [list(map(int,input().split())) for _ in range(n) ]
    result = 0
    for i in range(n) :
        for j in range(n):
            for d in dirs:
                ni = i + d[0]
                nj = j + d[1]
                # if 0 <= ni < n and 0 <= nj < n:
                #     temp = board[i][j] - board[ni][nj]
                #     # if temp > 0:
                #     #     result += temp
                #     # else :
                #     #     result -= temp
                #     # result += abs(board[i][j] - board[ni][nj])
                    
                #     result += temp if temp > 0 else -temp
                try :
                    result += abs(board[i][j]-board[ni][nj])
                except:
                    ...

    print(f'#{tc}', result)
    
# %%
# 부분 집합 구하기 (1)
# 재귀함수를 이용한 부분집합 구하기

def print_subset(bits, depth) :
    for i in range(2) :
        bits[depth] = i
        if depth >= len(bits)-1:
            print(bits)
        else:
            print_subset(bits, depth + 1)
               
bits = [0,0,0,0] 
print_subset(bits, 0) 

# 부분집합 구하기 (2)
# 비트 연산 이용
arr = [3,6,7]
n = len(arr)
# (1<<0) = 001
# (1<<1) = 010
# (1<<2) = 100
total = 0
for i in range(1<<n) :  # 1 << n == 2 ** n
    # print(f'b{str(bin(i))[2:]:0>3}')
    sub_sum = 0
    for j in range(n):   # 빠른 연산을 위해 비트 연산자를 사용
        if i & (1<<j):
            # print(arr[j], end = ', ')
            sub_sum += arr[j]
    total += sub_sum
    print() 

# %%
list1 = [[1,2,3,4,5,6],[7,8,9,10],[11,12,13]]

print(list1[0][1])
print(list1[0:2])


# %%
list1 = [[1,2,3],[4,5,6],[7,8,9]]

list1[0][1] = 10

print(list1)
# %%

list1 = list(range(10))
list[2:5] = 'k'
print(list1)

#%%
arr = [3,6,7]
n = len(arr)
# (1<<0) = 001
# (1<<1) = 010
# (1<<2) = 100
total = 0
for i in range(1<<n) :  # 1 << n == 2 ** n
    # print(f'b{str(bin(i))[2:]:0>3}')
    sub_sum = 0
    for j in range(n):   # 빠른 연산을 위해 비트 연산자를 사용
        if i & (1<<j):
            # print(arr[j], end = ', ')
            sub_sum += arr[j]
    total += sub_sum
    print() 
# %%
n =3
print(range(1<<n))
print(list(range(3,0,-1)))

# %%
str1 = ['cadsdff']
list1 = list(*str1)
list2 = list(input())
print(str1)
print(list2)