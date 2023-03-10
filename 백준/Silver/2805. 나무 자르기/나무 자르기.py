import sys
# 이분검색
if __name__=="__main__":
  N,M=map(int,input().split())
  tree=list(map(int,input().split()))
  lt=0
  rt=max(tree)
  ans=2147000000
  res=0
  while lt<=rt:
    mid=(lt+rt)//2
    sum=0 
    for i in tree:
      if i>mid:
        sum+=i-mid
    # 자른 나무가 넘치는 경우
    if sum>=M:
      lt=mid+1
      # 기존에 저장된 값보다 작을 때
      if ans>sum:
        ans=sum
        res=mid
    # 자른 나무가 부족한 경우
    else:
      rt=mid-1
  print(res)