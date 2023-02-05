import sys
import heapq as hq

# heapq 자료구조에 대한 이해가 필요하다.
# 부모노드가 자식노드보다 더 커야하고, 자식노드끼리는 상관x
input=sys.stdin.readline

heap=[]
val=int(input())

while val!=-1:
  if val==0:
    if len(heap)==0: # heap안에 아무것도 없으면 -1 출력
      print(-1)
    else:
      print(hq.heappop(heap))
  else:
    hq.heappush(heap,val)
  
  val=int(input())