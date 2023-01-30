import sys

# 이분검색, 결정알고리즘을 활용하는 아이디어는 기억이 났지만 구현이 제대로 되지 않았음.

input=sys.stdin.readline

N,C=map(int,input().split())

arr=[]
for i in range(N):
  arr.append(int(input()))

arr.sort()

def Count(mid):
  tmp=arr[0]
  cnt=1
  for i in range(N):
    if arr[i]-tmp>=mid:
      cnt+=1
      tmp=arr[i]
  return cnt

lt=1
rt=arr[N-1]
res=0
while lt<=rt:
  mid=(lt+rt)//2
  if Count(mid)>=C:
    res=max(res,mid)
    lt=mid+1
  else:
    rt=mid-1

print(res)