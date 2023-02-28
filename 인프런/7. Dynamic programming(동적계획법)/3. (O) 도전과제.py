import sys

# Bottom-up

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  dp=[0]*(N+1)
  dp[1]=1
  dp[2]=2
  for i in range(3,N+1):
    dp[i]=dp[i-1]+dp[i-2]
  print(dp[N])

# top-down 재귀 메모이제이션
# def DFS(L):
#   if dp[L]>0:
#     return dp[L]
#   if L==1 or L==2:
#     return L
#   else:
#     dp[L]=DFS(L-1)+DFS(L-2)
#     return dp[L]

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=int(input())
#   dp=[0]*(N+1)
#   print(DFS(N))