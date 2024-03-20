def make_set(n):
    parent = list(range(n+1))
    rank = [0] * (n+1)
    return parent, rank

def find_set(x):  # 대표자(루트)를 찾는 함수
    # while x != parent[x] :
    #     x = parent[x]
    # return x
    
    if parent[x] == x:
        return x
    # return find_set(parent[x])
    parent[x] = find_set(parent[x])
    return parent[x]

def union(x, y):
    root_x, root_y = find_set(x), find_set(y)
    if root_x != root_y :
        # 랭크가 더 높은 루트를 기준으로 합치기
        if rank[root_x] > rank[root_y] :
            parent[root_y] = root_x
        else:
            parent[root_x] = root_y
            if rank[root_x] == rank[root_y] :
                rank[root_y] += 1
    
        

parent, rank = make_set(6)  # 1~6번 노드
union(1,3)
union(2,3)
union(2,4)

union(5,6)

print(parent)


union(4, 6)
print(parent, rank)
