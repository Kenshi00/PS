import sys

def DFS(L):
  global ans
  if L==N:
    sum=0
    for i in range(N-1): #0~4
      sum+=abs(A[tmp[i]]-A[tmp[i+1]])
    ans=max(sum,ans)
  else:
    for i in res:
      if i not in tmp:
        tmp.append(i)
        DFS(L+1)
        tmp.pop()

if __name__=="__main__":
  N=int(input())
  A=list(map(int,input().split()))
  res=[x for x in range(N)]
  tmp=[]
  B=[]
  ans=-2147000000
  DFS(0)
  print(ans)