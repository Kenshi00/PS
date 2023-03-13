import sys
# 플로이드 워샬 알고리즘
if __name__=="__main__":
  input=sys.stdin.readline
  n=int(input())
  dis=[[100]*(n+1) for _ in range(n+1)]
  res=[0]*(n+1)
  # 입력정보를 통한 그래프 완성
  while True:
    a,b=map(int,input().split())
    if a==-1 and b==-1:
      break
    dis[a][b]=1
    dis[b][a]=1
  # 플로이드 워샬 알고리즘 적용
  for k in range(1,n+1):
    for i in range(1,n+1):
      for j in range(1,n+1):
          dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
  # 정답을 위한 자잘한 연산들
  for i in range(1,n+1):
    m=0
    for j in range(1,n+1):
      m=max(m,dis[i][j])
    res[i]=m
  res[0]=100
  score=min(res)
  candidate=[]
  for i in range(1,n+1):
    if res[i]==score:
      candidate.append(i)
  print(score,len(candidate))
  for i in candidate:
    print(i,end=' ')
