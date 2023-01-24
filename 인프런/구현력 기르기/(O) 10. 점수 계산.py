import sys

input=sys.stdin.readline

N=int(input())

arr=list(map(int,input().split()))
sum=0
cnt=0
for i in arr:
  if i==1:
    cnt+=1
    sum+=cnt
  else:
    cnt=0

print(sum)