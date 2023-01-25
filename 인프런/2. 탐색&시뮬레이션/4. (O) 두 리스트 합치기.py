import sys

input=sys.stdin.readline

N=int(input())
arr1=list(map(int,input().split()))
M=int(input())
arr2=list(map(int,input().split()))

# O(NlogN)
#res=arr1+arr2
# res.sort()

# O(N)
lt=0
rt=0
res=[]
while lt<len(arr1) and rt<len(arr2):
  if arr1[lt]<=arr2[rt]:
    res.append(arr1[lt])
    lt+=1
  else:
    res.append(arr2[rt])
    rt+=1

if lt<len(arr1):
  res+=arr1[lt:]
if rt<len(arr2):
  res+=arr2[rt:]

for i in res:
  print(i, end=' ')