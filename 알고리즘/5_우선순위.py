# 리슽트 활용 큐
numList = [1,2,3]
# 자료 삽입
numList.append(4)
# 자료 꺼내오는 경우
numList.pop(0)  # 시간 복잡도가 O(k)

#%%
from collections import deque

que = deque(maxlen = 500)  # 객체 선언, maxlen 생략 가능
# maxlen 이상의 값이 들어오면 자동으로 max_len을 늘림

# 값 추가
que.append(4)
que.append(2)

# 값 얻을 때
que.popleft()  # 4,  O(1)
que.popleft()  # 2

# %%
# 우선순위 큐  (코딩 테스트 자주 나옴)
# 우선순위가 높은 값을 먼저 얻음

from heapq import heapify, heappush, heappop

# heapify : 리스트를 우선순위 heap으로 변환
numList = [4,2,6,1,1,3]
heapify(numList)
print(numList)   # [1,1,3,4,2,6]
# 숫자 리스트인 경우 가장 작은 값을 먼저 얻음
print(numList[0])  # 우선순위가 가장 높은 값을 조회

# heappop : 우선순위가 높은 값을 반환
# 비어있으면 인덱스 에러
print(heappop(numList))
print(numList)

# heappush : item을 heap에 추가
heappush(numList, 0)
heappush(numList, 99)
print(numList)

numList = [-x for x in numList]
heapify(numList)
print(-numList[0])

#%%
fruits = [(3, '수박'), (3, '포도'), (5, '사과'), (0, '딸기')]
# 우선순위가 동등하면 2번째 요소로 우선순위를 판별

heapify(fruits)
print(heappop(fruits))
