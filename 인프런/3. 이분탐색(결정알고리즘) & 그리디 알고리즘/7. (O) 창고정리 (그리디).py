import sys
# 그리디는 언제나 정렬 우선!
input=sys.stdin.readline

L=int(input())
a=list(map(int,input().split()))
M=int(input())
a.sort() # a.sort(key=lambda x : x[0])

for i in range(M):
  a[0]+=1
  a[L-1]-=1
  a.sort()
print(a[L-1]-a[0])

# 내 풀이도 맞음
# for i in range(M):
#   x=a.index(max(a))
#   y=a.index(min(a))
#   a[x]-=1
#   a[y]+=1
# print(max(a)-min(a))