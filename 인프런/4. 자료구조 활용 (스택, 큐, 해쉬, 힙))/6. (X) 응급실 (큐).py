import sys
from collections import deque

# 튜플로 순서도 기억할 수 있다는 idea자체를 떠올리지 못함
# deque에 대한 활용도도 낮았음.

input=sys.stdin.readline

N,M=map(int,input().split())

# enumerate 사용시 index,value 반환
dq=[(pos,val) for pos,val in enumerate(list(map(int,input().split())))]
dq=deque(dq)

res=dq[M]

cnt=0
while dq:
  tmp=dq.popleft()
  maxx=max(dq,key=lambda x:x[1])
  # if any(tmp[1]<x[1] for x in dq) - any 함수(한개라도 참인게 있으면 True)
  if tmp[1]<maxx[1]:
    dq.append(tmp)
  else:
    cnt+=1
    if tmp==res:
      print(cnt)
      break
  
  
  