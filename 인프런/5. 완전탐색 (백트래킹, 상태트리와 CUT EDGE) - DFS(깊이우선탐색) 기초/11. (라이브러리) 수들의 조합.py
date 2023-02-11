import sys
import itertools as it

N,K=map(int,input().split())
a=list(map(int,input().split()))
m=int(input())
cnt=0
for x in it.combinations(a,K): # a에서 K개만큼 뽑는다
  if sum(x)%m==0:
    cnt+=1
print(cnt)