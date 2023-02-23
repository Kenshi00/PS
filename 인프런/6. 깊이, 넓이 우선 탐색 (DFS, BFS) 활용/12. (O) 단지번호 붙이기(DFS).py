import sys
# 원래 주어지는 board 배열과 ch 배열을 따로 만들었다.
# 방문할때마다 board의 1을 0으로 바꿔서 중복으로 세지 않게 하는 방법도 있다. 하지만 나는 체크배열도 만들어보고 싶어서 좀 복잡하게 했음.
def DFS(x,y):
  global L
  if board[x][y]==0 or ch[x][y]!=0:
    return
  else:
    ch[x][y]=L
    for i in range(4):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<N and 0<=yy<N and board[xx][yy]==1:
        DFS(xx,yy)

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  board=[list(map(int,input().rstrip())) for _ in range(N)]
  ch=[[0]*N for _ in range(N)]
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  res=[]

  L=0
  for i in range(N):
    for j in range(N):
      if board[i][j]==1 and ch[i][j]==0:
        L+=1
        DFS(i,j) 

  # 출력
  res=[0]*(L+1)
  for i in range(N):
    for j in range(N):
      res[ch[i][j]]+=1
  res=res[1:]
  res.sort()
  print(L)
  for i in res:
    print(i)
  