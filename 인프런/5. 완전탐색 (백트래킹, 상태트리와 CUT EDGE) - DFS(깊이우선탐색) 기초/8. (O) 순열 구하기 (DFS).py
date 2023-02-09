import sys

def DFS(L):
  global cnt
  if L==M:
    cnt+=1
    for i in res:
      print(i,end=' ')
    print()
    return
  else:
    for i in range(1,N+1):
      if ch[i]==0:
        ch[i]=1
        res[L]=i
        DFS(L+1)
        ch[i]=0
if __name__=="__main__":
  input=sys.stdin.readline
  N,M=map(int,input().split())
  res=[0]*M
  ch=[0]*(N+1)
  cnt=0
  DFS(0)
  print(cnt)