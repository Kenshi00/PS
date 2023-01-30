import sys

input=sys.stdin.readline

N,M=map(int,input().split())
a=list(map(int,input().split()))

 # 배열이 1~9라 치면 비디오가 9보다 작으면 어차피 9를 못넣기때문에 lt를 최소 9부터 시작해야 함 - 채팅에 좋은 아이디어라고 답글 남겨주심!
lt=max(a)
rt=sum(a)
res=sum(a)

while lt<=rt: # 이분검색 나오면 lt<=rt,lt<rt 문제마다 다름
  mid=(lt+rt)//2
  tmp=0
  cnt=1
  for j in a:
    tmp+=j
    if tmp>mid:
      cnt+=1
      tmp=j
  if cnt<=M: # 1,2,3개의 dvd만 사용할 용량이 될때 값 저장
    res=min(res,mid) # 30,20,17 다 답이 될수 있지만 우리가 구하는건 최소
    rt=mid-1
  else:
    lt=mid+1
print(res)

