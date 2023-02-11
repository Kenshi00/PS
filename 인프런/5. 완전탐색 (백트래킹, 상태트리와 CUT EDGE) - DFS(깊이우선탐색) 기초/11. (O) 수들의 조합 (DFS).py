import sys

def DFS(L,s):
  global cnt
  if L==K:
    if sum(res)%M==0:
      cnt+=1
  else:
    for i in range(s,N): # 0~4
      res[L]=arr[i]
      DFS(L+1,i+1)

if __name__=="__main__":
  input=sys.stdin.readline
  N,K=map(int,input().split())
  arr=list(map(int,input().split()))
  M=int(input())
  res=[0]*K
  cnt=0
  DFS(0,0)
  print(cnt)