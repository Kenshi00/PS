import sys

def DFS(x,y):
  global mx,my,nx,ny,cnt
  if x==mx and y==my:
    cnt+=1
    return
  else:
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<N and 0<=yy<N and map[x][y]<map[xx][yy]:
        DFS(xx,yy)

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  map=[list(map(int,input().split())) for _ in range(N)]
  cnt=0
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  # 출발, 도착 지점 정하기
  min=2147000
  max=-2147000
  for i in range(N):
    for j in range(N):
      if min>map[i][j]:
        min=map[i][j]
        nx=i
        ny=j
      if max<map[i][j]:
        max=map[i][j]
        mx=i
        my=j
  DFS(nx,ny)
  print(cnt)