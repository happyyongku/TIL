# %%

arr = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
new_arr =list(map(list,zip(*arr)))
print(new_arr)
#%%
a = True
while a:
    a = False
    if input() == '0':
        a = True
    else :
        a = False
        
#%%

list1 = [0,1,2,3,4,5,6,7,8]
list1 = list1[4:]
print(list1)


# %%
from collections import deque
list1 = deque([0,1,2,3,4,5,6,7,8])

list1[3]
#%%
arr = ['a', 'b', 'c']
n = len(arr)

def get_sub(tar):
		for i in range(n):
				if tar & 0x1:   # 비트 연산으로 마지막 자리를 검사
						print(arr[i], end = '')
				tar >>= 1

for tar in range(1<<n):
		print('{', end='')
		get_sub(tar)
		print('}')

#%%

from queue import PriorityQueue

list1 = [(1,0), (2,1), (3,1), (4,0)]
queue = PriorityQueue()
queue.put(*list1)
print(queue)

#%%
print(list(range(2, -1, -1)))