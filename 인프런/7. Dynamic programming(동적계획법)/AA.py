import sys

def DFS(s):
  global val,res
  for i in range(N):
    if s+arr[i][0]<=M:
      val+=arr[i][1]
      DFS(s+arr[i][0])
      res=max(val,res)
      val-=arr[i][1]
if __name__=="__main__":
  input=sys.stdin.readline
  N,M=map(int,input().split())
  arr=[]
  res=0
  val=0
  for _ in range(N):
    a,b=map(int,input().split())
    arr.append((a,b))
  DFS(0)
  print(res)