import sys

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  M=int(input())
  if M==0:
    print(len(str(N)))
    sys.exit(0)
  arr=list(map(int,input().split()))
  a=[x for x in range(10) if x not in arr]
  res=0
  cnt=2147000000
  for i in range(1000000):
    b=list(str(i))
    c=list(map(int,b))
    t=0
    for j in c:
      if j not in a:
        t+=1
    if t==0:
      if cnt>=abs(N-i):
        cnt=abs(N-i)
        res=i
      print(res)
  print(res)
