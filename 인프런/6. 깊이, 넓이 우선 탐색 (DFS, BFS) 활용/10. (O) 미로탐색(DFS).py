import sys
# L을 사용해 최단거리도 구할 수 있다. - 사실 문제 잘못읽고 구현한거.. 문제는 가짓 수 구하기다.
def DFS(L,tmp):
  global res
  if tmp==(6,6):
    res+=1
    return
  if tmp[0]<0 or tmp[0]>=7 or tmp[1]<0 or tmp[1]>=7 or board[tmp[0]][tmp[1]]==1:
    return
  else:
    # 방문할 때 1 표시
    board[tmp[0]][tmp[1]]=1
    for i in range(4):
      x=tmp[0]+dx[i]
      y=tmp[1]+dy[i]
      DFS(L+1,(x,y))
    # 방문 끝나고 나올 때 다시 0 표시
    board[tmp[0]][tmp[1]]=0
if __name__=="__main__":
  input=sys.stdin.readline
  board=[list(map(int,input().split())) for _ in range(7)]
  res=0
  dx=[-1,1,0,0]
  dy=[0,0,-1,1]
  DFS(0,(0,0))
  print(res)