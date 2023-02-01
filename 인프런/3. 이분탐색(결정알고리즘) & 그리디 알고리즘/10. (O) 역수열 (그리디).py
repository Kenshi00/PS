import sys

input=sys.stdin.readline

N=int(input())
a=list(map(int,input().split()))

# 이번엔 내 풀이가 더 간단
res=[]
for i in range(N,0,-1): # 1~8
  res.insert(a[i-1],i)

for i in res:
  print(i,end=" ")

# 선생님 답
# seq=[0]*N
# for i in range(N):
#   for j in range(N):
#     if a[i]==0 and seq[j]==0:
#       seq[j]=i+1
#       break
#     elif seq[j]==0:
#       a[i]-=1
# for i in seq:
#   print(i, end=' ')
