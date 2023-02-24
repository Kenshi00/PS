import sys
from collections import deque
# dis배열을 사용해서 거리 누적하면 편하다
if __name__=="__main__":
  input=sys.stdin.readline
  M,N=map(int,input().split())
  board=[list(map(int,input().split())) for _ in range(N)]
  dis=[[0]*M for _ in range(N)]
  dx=[0,0,-1,1]
  dy=[-1,1,0,0]
  dq=deque()
  res=[]
  for i in range(N):
    for j in range(M):
      if board[i][j]==1:
        dq.append((i,j))
  # 몇일 경과 후 토마토를 익힌다
  while dq:
    size=len(dq)
    for _ in range(size):
      tmp=dq.popleft()
      for k in range(4):
        x=tmp[0]+dx[k]
        y=tmp[1]+dy[k]
        if 0<=x<N and 0<=y<M and board[x][y]==0:
          board[x][y]=1
          dq.append((x,y))
          dis[x][y]=dis[tmp[0]][tmp[1]]+1
  # 모두 익지 못한 상황인지 확인 (0이 하나라도 있는지)
  for i in range(N):
    for j in range(M):
      if board[i][j]==0:
        print(-1)
        sys.exit()
  # 모두 익었다면 (0이 없고 1과-1로만 이루어져 있다면)
  m=-214700000
  for i in range(N):
    for j in range(M):
      m=max(dis[i][j],m)
  print(m)