import sys
# 역시 규칙을 통해 dp배열을 만들어 줘야함.
input=sys.stdin.readline
N=int(input())
a=list(map(int,input().split()))
dp=[1]*N
for i in range(N): # 0~7
  for j in range(i+1): # ~0, ~1, ~2...
    if a[i]>a[j]:
      dp[i]=max(dp[j]+1,dp[i])
print(max(dp))


# DFS로 구현은 했으나 시간초과
# def DFS(s):
#   global cnt
#   cnt=max(cnt,len(res))
#   for i in range(s+1,N):
#     if a[s]<a[i]:
#       res.append(a[i])
#       DFS(i)
#       res.pop()

# if __name__=="__main__":
#   input=sys.stdin.readline
#   N=int(input())
#   a=list(map(int,input().split()))
#   res=[]
#   cnt=0
#   for i in range(N):
#     res.append(a[i])
#     DFS(i)
#     res.pop()
#   print(cnt)