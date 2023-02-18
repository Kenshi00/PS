import sys
from collections import deque
# L==N//2 의 격자 아이디어를 떠올리는건 불가능에 가까움. 그냥 외우자. DFS, BFS는 항상 level이 연관되어 있음. 꼭 떠올려야 한다.
if __name__=="__main__":
  input=sys.stdin.readline
  dx=[0,0,-1,1]
  dy=[-1,1,0,0]
  N=int(input())
  a=[list(map(int,input().split())) for _ in range(N)]
  ch=[[0]*N for _ in range(N)] # 2차원 체크배열
  sum=0
  Q=deque()
  ch[N//2][N//2]=1
  sum+=a[N//2][N//2]
  Q.append((N//2,N//2))
  L=0
  while Q:
    if L==N//2:
      break
    size=len(Q)
    for i in range(size):
      tmp=Q.popleft()
      for j in range(4):
        x=tmp[0]+dx[j]
        y=tmp[1]+dy[j]
        if ch[x][y]==0:
          Q.append((x,y))
          sum+=a[x][y]
          ch[x][y]=1
    L+=1
  print(sum)



# BFS 사용x 풀이
# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=int(input())
#   a=[list(map(int,input().split())) for _ in range(N)]
#   s=e=N//2
#   answer=0
#   for i in range(N): #0~4
#     answer+=sum(a[i][s:e+1])
    
#     if i<N//2:
#       s-=1
#       e+=1
#     else:
#       s+=1
#       e-=1
#   print(answer)