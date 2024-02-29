# %%
list1 = [list(map(str, input())) for _ in range(2)]
list2 = [input() for _ in range(2)]
print(list1)
print(list2)
#%%
list3 = [0,1,2,3,4,5,6,7,8,9]
length = len(list3)
list3[:6] = []
print(length)
print(len(list3))
print(list3)

#%%
list1 = [0,1,2,3,4,5,6,7,8,9]
list1[3:6] = 9
print(list1)

#%%
n = 4

for i in range(n):
    arr = [0] * n
    arr[0], arr[i] = 1, 1
    print(arr)
# %%
list1 = []
a = '3'
b = '*'
c = '4'
list1.append(eval(a+b+c))
print(list1)

print(a*b+c)
#%%
list1 = []
print(sum(list1))
print(list1[0])
#%%
a = [(1,2)]

b, c = a.pop(0)
print(b, c)
#%%
list1 = [1,2,3,4,5,6,7]
exlist = [0]*1
for i in range(0):
    print(i)
#%%
str1 = 'abcd'
print('e' + str1)

# %%
list1 = ['0000','0000','0000','1111','1111','0011']
print(set(list1))

#%%

arr = [[1,2,3],[4,5,6],[7,8,9]]
new_arr =list(map(list,zip(*arr)))
print(new_arr)