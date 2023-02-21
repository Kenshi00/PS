import sys
from collections import deque
# 큐를 이용한 문제

if __name__=="__main__":
  input=sys.stdin.readline
  N,K=map(int,input().split())
  dq=deque(range(1,N+1))
  res=[]
  cnt=1
  while dq:
    tmp=dq.popleft()
    if cnt==K:
      res.append(tmp)
      cnt=0
    else:
      dq.append(tmp)
    cnt+=1
  res=[str(x) for x in res]
  print('<'+', '.join(res)+'>')