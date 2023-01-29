import sys

input=sys.stdin.readline

K,N = map(int,input().split())
a=[]

for i in range(K):
  a.append(int(input()))

# 결정 알고리즘 - 정답의 일정 범위를 정해서 다 해본다!
# lt, rt를 이용한 이분검색으로 해야함 - time limit 때문에

lt=1
rt=max(a) # 802
res=0
while lt<rt:
  cnt=0
  mid=(lt+rt)//2 # 400
  for j in a: # j = 802, 743, 457, 539
    cnt+=(j//mid)
  if cnt>=N:
    res=max(res,mid)
    lt=mid+1
  else:
    rt=mid-1

print(res)