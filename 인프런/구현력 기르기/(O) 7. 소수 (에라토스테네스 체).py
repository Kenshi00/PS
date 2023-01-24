import sys

input=sys.stdin.readline

N=int(input())
arr=[0]*(N+1)

res=[] # result
count=0
for i in range(2,N+1):
  if arr[i]==0: # 0이면 cnt 1 증가
    count+=1
  for i in range(2*i,N+1,i): # i의 배수를 다 1로 바꿔준다.
    if arr[i]==0:
      arr[i]=1

print(count)