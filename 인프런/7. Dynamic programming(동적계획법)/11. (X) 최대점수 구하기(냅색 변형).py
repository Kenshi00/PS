import sys
# 냅색 알고리즘의 변형 - dy배열 접근을 거꾸로
if __name__=="__main__":
  n,m=map(int,input().split())
  dy=[0]*(m+1)
  for i in range(n):
    ps,pt=map(int,input().split())
    for j in range(m,pt-1,-1):
      dy[j]=max(dy[j],dy[j-pt]+ps)
  print(dy[m])