import sys
from collections import deque
# 중복되지 않도록 1을 방문할 시 0으로 바꿔주는게 POINT
if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  board=[list(map(int,input().split())) for _ in range(N)]
  dq=deque()
  dx=[-1,1,0,0,1,1,-1,-1]
  dy=[0,0,-1,1,-1,1,-1,1]
  cnt=0
  for i in range(N):
    for j in range(N):
      if board[i][j]==1:
        cnt+=1 # 한 개의 섬을 찾음
        board[i][j]=0 # 다음 섬 때 중복되지 않기 위해
        dq.append((i,j))
        # BFS
        while dq:
          size=len(dq) # 여기선 size 필요 없지만 Level을 세야하는 경우 필요함. 그냥 웬만하면 해주자
          for _ in range(size):
            tmp=dq.popleft()
            for k in range(8):
              x=tmp[0]+dx[k]
              y=tmp[1]+dy[k]
              if 0<=x<N and 0<=y<N and board[x][y]==1:
                board[x][y]=0
                dq.append((x,y))
  print(cnt)