import sys

input=sys.stdin.readline

N=int(input())

# 간단한 코드

arr=[list(map(int,input().split())) for _ in range(N)]

# 내 코드

# arr=[]
# for i in range(N):
#   arr.append(list(map(int,input().split())))

res=[]

for i in range(N):
  row=column=0
  for j in range(N):
    row+=arr[i][j]
    column+=arr[j][i]
  res.append(row)
  res.append(column)

rec1=0
rec2=0
for i in range(N):
  rec1+=arr[i][i]
  rec2+=arr[i][N-i-1]

res.append(rec1)
res.append(rec2)
print(max(res))