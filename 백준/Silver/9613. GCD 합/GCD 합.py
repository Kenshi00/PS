import sys

def GCD(a,b):
  if b==0:
    return a
  else:
    return GCD(b,a%b)

if __name__=="__main__":
  input=sys.stdin.readline
  t=int(input())
  for _ in range(t):
    n=list(map(int,input().split()))
    sum=0
    for i in range(1,len(n)):
      for j in range(i+1,len(n)):
        a=n[i]
        b=n[j]
        sum+=GCD(a,b)
    print(sum)