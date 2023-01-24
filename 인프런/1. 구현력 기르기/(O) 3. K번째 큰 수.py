import sys

input=sys.stdin.readline

N,K = map(int ,input().split())
arr=list(map(int, input().split()))

res=set() # set은 중복을 제거해준다.
for i in range(N):
  for j in range(i+1,N):
    for k in range(j+1,N):
      num = arr[i]+arr[j]+arr[k]
      res.add(num) #
res=list(res)
res.sort(reverse=True)
print(res[K-1])

