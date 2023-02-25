import sys
from collections import deque
# DFS 조합 사용
def DFS(L,s):
  global ans
  # 조합이 하나 완성됐을때
  if L==M:
    sum=0
    for j in hs:
      dis=214700000
      for k in res: # 얘는 6개 다하면 안됨 4개만
        tmp=abs(j[0]-dq[k][0])+abs(j[1]-dq[k][1])
        dis=min(dis,tmp)
      # 한 조합 상황의 도시 피자 배달거리 -> sum
      sum+=dis
    # 한 상황이 발생할 때마다 최소거리 비교
    ans=min(ans,sum)
          
  else:
    for i in range(s,len(dq)): # 1 ~ 5
      res[L]=i
      DFS(L+1,i+1)

if __name__=="__main__":
  input=sys.stdin.readline
  N,M=map(int,input().split())
  board=[list(map(int,input().split())) for _ in range(N)]
  hs=deque()
  ans=214700000
  dq=deque()
  res=[0]*M
  for i in range(N):
    for j in range(N):
      if board[i][j]==2:
        dq.append((i,j))
      elif board[i][j]==1:
        hs.append((i,j))
  DFS(0,0)
  print(ans)