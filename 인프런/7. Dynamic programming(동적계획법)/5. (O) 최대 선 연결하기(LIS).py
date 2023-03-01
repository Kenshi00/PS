import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  a=list(map(int,input().split()))
  dp=[1]*N
  for i in range(N):
    for j in range(i+1):
      if a[i]>a[j]:
        dp[i]=max(dp[j]+1,dp[i])
  print(max(dp))
