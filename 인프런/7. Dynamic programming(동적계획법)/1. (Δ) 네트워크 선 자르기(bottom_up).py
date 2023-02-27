import sys

# DP - dynamic programming
# 점화식(규칙)을 구해야한다.

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  dp=[0]*(N+1)
  dp[1]=1
  dp[2]=2
  for i in range(3,N+1):
    dp[i]=dp[i-1]+dp[i-2]
  print(dp[N])
# DFS로 짰는데 시간초과남
# def DFS(s):
#   global cnt
#   if s==N:
#     cnt+=1
#     return 
#   if s>N:
#     return
#   else:
#     for i in range(1,3):
#       res.append(i)
#       DFS(s+i)
#       res.pop()

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=int(input())
#   res=[]
#   cnt=0
#   DFS(0)
#   print(cnt)