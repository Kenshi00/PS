import sys

input=sys.stdin.readline

N,M=map(int, input().split())

a=list(map(int,input().split()))

a.sort()
print(a)
lt=0
rt=N-1
while lt<=rt:
  tmp=lt+rt//2
  if M==a[tmp]:
    print(tmp+1)
    break
  elif M<a[tmp]:
    rt=tmp-1
  else:
    lt=tmp+1
