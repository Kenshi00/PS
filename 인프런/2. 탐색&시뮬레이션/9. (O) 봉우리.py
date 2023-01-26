import sys

input=sys.stdin.readline

N=int(input())

arr=[list(map(int,input().split())) for _ in range(N)]


x=[0,0,-1,1]
y=[-1,1,0,0]

# 가장자리에 0으로 감싸고,
arr.insert(0,[0]*N)
arr.append([0]*N)
for i in arr:
  i.insert(0,0)
  i.append(0)
# 파이썬의 all 함수를 이용하여 간단히 구현
res=0
for i in range(1,N+1):
  for j in range(1,N+1):
    if all(arr[i][j]>arr[i+x[k]][j+y[k]] for k in range(4)):
      res+=1
print(res)

# 나의 풀이도 맞음!
# for i in range(N):
#   for j in range(N):
#     cnt=0
#     for k in range(4):
#       if i+x[k]<0 or i+x[k]>=N or j+y[k]<0 or j+y[k]>=N:
#         continue
#       elif arr[i+x[k]][j+y[k]]<arr[i][j]:
#         continue
#       else:
#         cnt+=1
#     if cnt==0:
#       res+=1
# print(res)