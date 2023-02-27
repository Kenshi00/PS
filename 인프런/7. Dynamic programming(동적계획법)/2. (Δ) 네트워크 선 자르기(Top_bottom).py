import sys
# Top-Down : 재귀, 메모이제이션(Cut Edge)

def DFS(L):
  # 이미 구한놈이면 DFS가지 뻗지 말고 값을 바로 줌
  if dp[L]>0:
    return dp[L]
  if L==1 or L==2:
    return L
  # 이전에 구했어도 처음부터 다시 구해서 return 해줌
  else:
    dp[L]=DFS(L-1)+DFS(L-2)
    return dp[L]
if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  dp=[0]*(N+1)
  dp[1]=1
  dp[2]=2
  DFS(N)
  print(dp[N])