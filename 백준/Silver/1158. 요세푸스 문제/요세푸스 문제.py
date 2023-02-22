import sys
from collections import deque

# 큐를 이용한 문제
# list말고 deque를 써야 시간초과가 안난다. pop(0)는 시간복잡도 O(n)이지만 deque의 popleft()는 O(1)임 - 웬만하면 deque를 쓰자!
# append(str(tmp))로 하면 while문 돌때마다 str()이 실행되서 시간초과남..

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