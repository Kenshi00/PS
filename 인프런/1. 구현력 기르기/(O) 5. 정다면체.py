import sys

input=sys.stdin.readline

N,M = map(int, input().split())

arr=[]
answer=[0]*(N+M+1)

for i in range(1,N+1):
  for j in range(1,M+1):
    answer[i+j]+=1

for y in range(len(answer)):
  if answer[y]==max(answer):
    print(y, end=' ')