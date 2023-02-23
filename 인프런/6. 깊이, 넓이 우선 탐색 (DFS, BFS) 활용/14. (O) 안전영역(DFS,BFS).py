import sys
from collections import deque
# 격자판 탐색은 DFS BFS 모두 가능
if __name__=="__main__":

  # 초기 변수 및 배열 선언
  input=sys.stdin.readline
  N=int(input())
  board=[list(map(int,input().split())) for _ in range(N)]
  res=[]
  dx=[0,0,-1,1]
  dy=[-1,1,0,0]

  # 최대 높이 지정
  m=-21470000
  for i in range(N):
    for j in range(N):
      m=max(m,board[i][j])
  # 백준 기준 높이를 0부터 해야 한다고 한다.
  for h in range(m+1): # 0~9
    # 체크배열 1과 0으로 설정
    ch=[[1]*N for _ in range(N)]

    for i in range(N):
      for j in range(N):
        if board[i][j]<=h:
          ch[i][j]=0

    # BFS
    dq=deque()
    cnt=0
    for i in range(N):
      for j in range(N):
        if ch[i][j]==1:
          ch[i][j]=0
          cnt+=1
          dq.append((i,j))
          while dq:
            size=len(dq)
            for _ in range(size):
              tmp=dq.popleft()
              for k in range(4):
                x=tmp[0]+dx[k]
                y=tmp[1]+dy[k]
                if 0<=x<N and 0<=y<N and ch[x][y]==1:
                  ch[x][y]=0
                  dq.append((x,y))

    res.append(cnt)
  print(max(res))