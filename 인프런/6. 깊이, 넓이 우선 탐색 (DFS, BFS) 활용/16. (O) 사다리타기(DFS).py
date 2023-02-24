import sys
# 난 0~9 까지 다했음 - 비효율적

def DFS(x,y):
  global res
  if x==0:
    res=y
  else:
    for i in range(3):
      xx=x+dx[i]
      yy=y+dy[i]
      if 0<=xx<10 and 0<=yy<10 and board[xx][yy]==1 and dis[xx][yy]==0:
        dis[xx][yy]=1
        DFS(xx,yy)
        dis[xx][yy]=0
        break

if __name__=="__main__":
  input=sys.stdin.readline
  board=[list(map(int,input().split())) for _ in range(10)]
  dx=[0,0,-1]
  dy=[-1,1,0]
  res=0
  dis=[[0]*10 for _ in range(10)]
  for i in range(10): #0~9
    if board[9][i]==2:
      dis[9][i]=1
      DFS(9,i)
      dis[9][i]=0
  print(res)

# def DFS(x,y):
#   global res
#   for i in range(3):
#     xx=x+dx[i]
#     yy=y+dy[i]
#     if 0<=xx<10 and 0<=yy<10 and 1<=board[xx][yy]<=2 and dis[xx][yy]==0:
#       dis[xx][yy]=1
#       # for j in dis:
#       #   print(j)
#       if board[xx][yy]==2:
#         print(res)
#         sys.exit()
#       DFS(xx,yy)
#       dis[xx][yy]=0
#       break

# if __name__=="__main__":
#   input=sys.stdin.readline
#   board=[list(map(int,input().split())) for _ in range(10)]
#   dx=[0,0,1]
#   dy=[-1,1,0]
#   dis=[[0]*10 for _ in range(10)]
#   for i in range(10):
#     if board[0][i]==1:
#       res=i
#       dis[0][i]=1
#       DFS(0,i)
#       dis[0][i]=0
  