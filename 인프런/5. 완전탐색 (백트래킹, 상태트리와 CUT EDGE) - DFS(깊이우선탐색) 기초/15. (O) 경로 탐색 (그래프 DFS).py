import sys

def DFS(L):
  global cnt
  if L==N:
    cnt+=1
    for x in path:
      print(x, end=' ')
    print()
  else:
    for i in range(1,N+1): # 1~5
      if ch[i]==0 and a[L][i]==1:
        ch[i]=1
        path.append(i)
        DFS(i)
        path.pop()
        ch[i]=0
if __name__=="__main__":
  input=sys.stdin.readline
  N,M=map(int,input().split())
  a=[[0]*(N+1) for _ in range(N+1)]
  for _ in range(M):
    i,j=map(int,input().split())
    a[i][j]=1
  cnt=0
  path=[]
  path.append(1)
  ch=[0]*(N+1)
  ch[1]=1
  DFS(1)
  print(cnt)