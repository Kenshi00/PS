import sys

def DFS(L):
  global cnt
  if L==M:
    for i in res:
      print(i,end=' ')
    print()
    cnt+=1
    return
  else:
    for i in range(1,N+1):
      res[L]=i
      DFS(L+1)
if __name__=="__main__":
  input=sys.stdin.readline
  N,M=map(int,input().split())
  res=[0]*M
  cnt=0
  DFS(0)
  print(cnt)