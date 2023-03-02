import sys

# bottom-up - 쉽다!
# if __name__=="__main__":
#   n=int(input())
#   arr=[list(map(int,input().split())) for _ in range(n)]
#   dy=[[0]*n for _ in range(n)]
#   dy[0][0]=arr[0][0]
#   for i in range(n):
#     dy[0][i]=dy[0][i-1]+arr[0][i]
#     dy[i][0]=dy[i-1][0]+arr[i][0]
#   for i in range(1,n):
#     for j in range(1,n):
#       dy[i][j]=min(dy[i-1][j], dy[i][j-1])+arr[i][j]
#   print(dy[n-1][n-1])

# top-down - ㅈㄴ 어려움

# def DFS(x,y):
#   if dy[x][y]>0:
#      return dy[x][y]
#   if x==0 and y==0:
#       return arr[0][0]
#   else:
#     if y==0:
#        dy[x][y]=DFS(x-1,y)+arr[x][y]
#     elif x==0:
#        dy[x][y]=DFS(x,y-1)+arr[x][y]
#     else:
#        dy[x][y]=min(DFS(x-1,y), DFS(x,y-1))+arr[x][y]
#     return dy[x][y]
  
# if __name__=="__main__":
#     n=int(input())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     dy=[[0]*n for _ in range(n)]
#     print(DFS(n-1,n-1))

# 내가한건 짬뽕인듯
# def DFS(x,y):
#   if x==N-1 and y==N-1:
#     return
#   else:
#     for i in range(2):
#       xx=x+dx[i]
#       yy=y+dy[i]
#       if 0<=xx<N and 0<=yy<N and dis[xx][yy]>dis[x][y]+a[xx][yy]:
#         dis[xx][yy]=dis[x][y]+a[xx][yy]
#         DFS(xx,yy)
# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=int(input())
#   a=[list(map(int,input().split())) for _ in range(N)]
#   dis=[[2147000000]*N for _ in range(N)]
#   dis[0][0]=a[0][0]
#   dx=[0,1]
#   dy=[1,0]
#   DFS(0,0)
#   print(dis[N-1][N-1])