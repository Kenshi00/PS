import sys
from collections import deque
# 최단거리는 무조건 BFS
# 거리 배열을 따로 만들어줘서 숫자를 더해가도 됨
if __name__=="__main__":
  input=sys.stdin.readline
  graph=[]
  dq=deque()
  for i in range(7):
    a=list(map(int,input().split()))
    graph.append(a)
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  dq.append((0,0))
  L=0
  while dq:
    size=len(dq)
    for _ in range(size):
      tmp=dq.popleft()
      if tmp==(6,6):
        print(L)
        sys.exit()
      graph[tmp[0]][tmp[1]]=1
      for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<7 and 0<=y<7 and graph[x][y]==0:
          dq.append((x,y))
    L+=1
  print(-1)