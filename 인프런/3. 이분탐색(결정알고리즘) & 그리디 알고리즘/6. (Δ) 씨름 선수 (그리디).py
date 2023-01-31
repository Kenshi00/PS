import sys

# 그리디는 정렬로 푸는게 효과적임을 기억하자.
# 키 순으로 정렬한 후에 이중 for문이 아닌 max 값을 이용해서 시간복잡도를 낮게 할 수 있는데 못했음.

input=sys.stdin.readline

N=int(input())
arr=[]
for i in range(N):
  x,y=map(int,input().split())
  arr.append((x,y))

arr.sort(key=lambda x : -x[0])

cnt=0
largest=0
for i in range(N):
  if largest<arr[i][1]:
    cnt+=1
    largest=arr[i][1]
print(cnt)


# 내 풀이도 맞음
# res=0
# for h,w in arr:
#   cnt=0
#   for x,y in arr:
#     if h<x and w<y:
#       cnt+=1
#   if cnt==0:
#     res+=1
# print(res)
