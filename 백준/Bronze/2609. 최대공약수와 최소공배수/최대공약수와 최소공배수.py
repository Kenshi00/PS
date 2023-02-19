import sys

def GCD(a,b):
  global div
  if a==0 or b==0:
    div=max(a,b)
  else:
    if a>b:
      GCD(a%b,b)
    else:
      GCD(a,b%a)
if __name__=="__main__":
  input=sys.stdin.readline
  a,b=map(int,input().split())
  div=0
  GCD(a,b)
  print(div)
  print((a//div)*(b//div)*div)