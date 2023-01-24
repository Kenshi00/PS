import sys

input=sys.stdin.readline

N=int(input())
res=[]

def dice(x):
  if x[0]==x[1]==x[2]:
    return 10000+x[0]*1000
  elif x[0]==x[1]:
    return 1000+x[0]*100
  elif x[0]==x[2]:
    return 1000+x[0]*100
  elif x[1]==x[2]:
    return 1000+x[1]*100
  else:
    return max(x)*100

for i in range(N):
  arr=list(map(int,input().split()))
  res.append(dice(arr))

print(max(res))