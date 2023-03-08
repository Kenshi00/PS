import sys
# 완전탐색 - brute force
if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  M=int(input())
  if M==0:
    print(min(abs(N-100),len(str(N))))
    sys.exit(0)
  arr=list(map(int,input().split()))
  a=[x for x in range(10) if x not in arr]
  res=0
  # 현재 채널에서 + 혹은 -만 사용하여 이동하는 경우
  cnt=abs(N-100)

  for i in range(1000001):
    b=list(str(i))
    c=list(map(int,b))
    t=0
    for j in c:
      if j not in a:
        t+=1
    # 각 숫자가 고장이 안난 경우만 실행
    if t==0:
      tmp=abs(N-i)+len(str(i))
      if cnt>tmp:
        cnt=tmp
  print(cnt)
