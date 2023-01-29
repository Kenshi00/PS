import sys

input=sys.stdin.readline

N,M=map(int, input().split())

a=list(map(int,input().split()))

a.sort()

lt=0
rt=N-1
# 이분검색 할 때 이 while lt<=rt 조건 기억하기!
while lt<=rt:
  mid=(lt+rt)//2
  if M==a[mid]:
    print(mid+1)
    break
  elif M<a[mid]:
    rt=mid-1
  else:
    lt=mid+1
