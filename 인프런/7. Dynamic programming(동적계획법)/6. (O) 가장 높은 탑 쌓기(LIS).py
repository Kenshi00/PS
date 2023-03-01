import sys
# 튜플은 immutable해서 그 값을 바꿀 수 없다.
input=sys.stdin.readline

N=int(input())
arr=[]
for i in range(N):
  a,b,c=map(int,input().split())
  arr.append((a,b,c))
arr.sort()
dp=[]
for i in range(N):
  dp.append(arr[i][1])

for i in range(N):
  tmp=0
  for j in range(i+1):
    if arr[i][2]>arr[j][2]:
      tmp=max(dp[j],tmp)
  dp[i]+=tmp
print(max(dp))