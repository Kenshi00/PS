import sys

def fac(n):
  if n==0:
    return 1
  else:
    return n*fac(n-1)

if __name__=="__main__":
  input=sys.stdin.readline
  N=int(input())
  tmp=str(fac(N))
  cnt=0
  for i in reversed(tmp):
    if i!='0':
      break
    cnt+=1
  print(cnt)