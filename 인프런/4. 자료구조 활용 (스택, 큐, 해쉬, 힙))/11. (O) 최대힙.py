
# heapq에서는 최대 힙을 제공하지 않는다.
# 그래서 부호를 변경하는 방법을 사용해서 최대힙 구현
# 부호를 바꿔서 최소 힙에 넣어준 뒤에 최솟값부터 pop할때 다시 바꿔준다.

import sys
import heapq as hq

heap=[]
while True:
  a=int(input())
  if a==-1:
    break
  if a==0:
    if len(heap)==0:
      print(-1)
    else:
      print(-(hq.heappop(heap)))
  else:
    hq.heappush(heap,-a)

